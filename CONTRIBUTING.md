# Contributing to docker-practice

👋 Thank you for considering contributing to **docker-practice**!  
This project is a community-driven, unofficial repository designed to help people prepare for the **Docker Certified Associate (DCA)** certification exam.

---

## 🚦 Code of Conduct

- Be respectful and constructive.
- No spam, trolling, or off-topic content.
- This is a learning-focused and inclusive project.

---

## ✅ What you can contribute

We welcome contributions such as:

- ✅ New YAML quiz files for DCA topics
- ✅ Improvements to existing questions (clarity, accuracy, formatting)
- ✅ Helpful links to official documentation (Docker or Mirantis)
- ✅ Typos or syntax corrections
- ✅ README or documentation improvements

---

## 🚫 What NOT to contribute

To keep the project safe and legal:

- ❌ **Do NOT copy or reproduce any proprietary content** from:
    - Docker Inc.
    - Mirantis
    - Official training guides or exam dumps

- ❌ Do NOT submit:
    - Official exam questions (real or leaked)
    - Screenshots, PDFs, or copyrighted material

All questions must be **original, community-created**, and **based only on public documentation**.

---

## 🧩 Structure of quiz files

All questions must be written in [YAML](https://yaml.org/) format with this structure:

```yaml
questions:
  - uuid: 123e4567-e89b-12d3-a456-426614174000
    question: What is the default network driver in Docker?
    answers:
      - { value: 'bridge', correct: true }
      - { value: 'host', correct: false }
      - { value: 'overlay', correct: false }
      - { value: 'macvlan', correct: false }
    help: https://docs.docker.com/network/
```
* 🧠 Use unique uuids (you can use uuidgenerator.net)
* 🔗 Prefer links to official Docker or Mirantis documentation in the help field
## 🛡️ Legal Notice

This is an unofficial, independent, and open-source project.
By contributing, you confirm that:
* All your content is original
* You have not copied any official exam content
* You agree to license your contributions under the MIT License

## 📬 How to contribute
* Fork the repo
* Create a new branch for your contribution
* Add your files or edits
* Open a pull request with a clear description of your changes

We’ll review your submission as quickly as possible. 🙏