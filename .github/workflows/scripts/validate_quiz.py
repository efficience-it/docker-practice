import os
import sys
import re
import uuid
import yaml

def is_valid_uuid4(val):
    try:
        return str(uuid.UUID(val, version=4)) == val
    except ValueError:
        return False

def is_valid_url(url):
    return re.match(r"^https?://[^\s]+$", url) is not None

def validate_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"YAML Error in {file_path}: {exc}")
            return False

    errors = []

    if not isinstance(data, dict) or 'questions' not in data:
        errors.append(f"File {file_path} must have a top-level key 'questions'.")
        return False

    for i, question in enumerate(data['questions']):
        if not isinstance(question, dict):
            errors.append(f"Question {i + 1} in {file_path} is not a dictionary.")
            continue

        uuid_ = question.get('uuid')
        if not uuid_ or not is_valid_uuid4(uuid_):
            errors.append(f"Question {i + 1} in {file_path} has an invalid or missing UUID.")

        qtext = question.get('question', '').strip()
        if len(qtext) < 3:
            errors.append(f"Question {i + 1} ('{qtext}') in {file_path} must have at least 3 characters.")

        if 'answers' not in question or not isinstance(question['answers'], list):
            errors.append(f"Question {i + 1} in {file_path} is missing 'answers' or it is not a list.")
            continue

        correct_answers = []
        for j, answer in enumerate(question['answers']):
            val = answer.get('value', '').strip()
            if len(val) < 1:
                errors.append(f"Answer {j + 1} ('{val}') for question {i + 1} in {file_path} must have at least 1 character.")
            if answer.get('correct') is True:
                correct_answers.append(answer)

        if not correct_answers:
            errors.append(f"Question {i + 1} ('{qtext}') in {file_path} does not have any correct answers.")

        if 'help' not in question:
            errors.append(f"Question {i + 1} in {file_path} is missing the 'help' field.")
        elif not is_valid_url(question['help']):
            errors.append(f"Question {i + 1} in {file_path} has an invalid URL in 'help': {question['help']}")

    if errors:
        for error in errors:
            print(f"Error: {error}")
        return False

    return True

def validate_all_files(directory):
    all_valid = True
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                print(f"Validating {file_path}")
                if not validate_yaml(file_path):
                    all_valid = False
    return all_valid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_quiz.py <path_to_directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not validate_all_files(directory):
        sys.exit(1)
