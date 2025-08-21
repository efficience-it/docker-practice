# docker-practice

### Domain 1: Orchestration (25% of exam)

* [Complete the setup of a swarm mode cluster, with managers and worker nodes](data/1_Orchestration/complete_setup_swarm_mode_cluster_managers_worker_nodes.yaml)
* Describe and demonstrate how to extend the instructions to run individual containers into running services under swarm.
* [Describe the importance of quorum in a swarm cluster.](data/1.Orchestration/describe_importance_quorum_swarm_cluster.yaml)
* [Describe the difference between running a container and running a service.](data/1_Orchestration/describe_difference_between_running_container_and_service.yaml)
* [Interpret the output of “docker inspect” commands.](data/1_Orchestration/interpret_output_docker_inspect_commend.yaml)
* Convert an application deployment into a stack file using a YAML compose file with "docker stack deploy"
* [Manipulate a running stack of services.](data/1_Orchestration/manipulate_stacks.yaml)
* Describe and demonstrate orchestration activities.
* [Increase the number of replicas.](data/1_Orchestration/increase_the_number_of_replicas.yaml)
* [Add networks, publish ports.](data/1_Orchestration/add_networks_publish_ports.yaml)
* [Mount volumes.](data/1_Orchestration/mount_volumes.yaml)
* Describe and demonstrate how to run replicated and global services.
* [Apply node labels to demonstrate placement of tasks.](data/1_Orchestration/apply_node_labels_placement_tasks.yaml)
* Describe and demonstrate how to use templates with “docker service create”.
* Identify the steps needed to troubleshoot a service not deploying.
* Describe how a Dockerized application communicates with legacy systems.
* Describe how to deploy containerized workloads as Kubernetes pods and deployments.
* Describe how to provide configuration to Kubernetes pods using configMaps and secrets.

### Domain 2: Image Creation, Management, and Registry (20% of exam)

* [Describe the use of Dockerfile.](data/2_Image_creation_management_registry/describe_the_use_of_dockerfile.yaml)
* [Describe options, such as add, copy, volumes, expose, entry point.](data/2_Image_creation_management_registry/identify_display_main_parts_dockerfile.yaml)
* [Identify and display the main parts of a Dockerfile.](data/2_Image_creation_management_registry/identify_display_main_parts_dockerfile.yaml)
* [Describe and demonstrate how to create an efficient image via a Dockerfile.](data/2_Image_creation_management_registry/describe_demonstrate_how_create_efficient_image_via_dockerfile.yaml)
* [Describe and demonstrate how to use CLI commands to manage images, such as list, delete, prune, rmi.](data/2_Image_creation_management_registry/describe_demonstrate_how_use_cli_command_manage_images_list_delete_prune_rmi.yaml)
* [Describe and demonstrate how to inspect images and report specific attributes using filter and format](data/2_Image_creation_management_registry/describe_demonstrate_how_to_inspec_images_report_specifi_attributes_using_filter_format.yaml)
* [Describe and demonstrate how to tag an image.](data/2_Image_creation_management_registry/describe_demonstrate_how_to_tag_image.yaml)
* Describe and demonstrate how to apply a file to create a Docker image.
* Describe and demonstrate how to display layers of a Docker image
* Describe and demonstrate how to modify an image to a single layer.
* Describe and demonstrate registry functions.
* [Deploy a registry.](data/2_Image_creation_management_registry/deploy_registry.yaml)
* [Log into a registry.](data/2_Image_creation_management_registry/log_into_a_registry.yaml)
* [Utilize search in a registry.](data/2_Image_creation_management_registry/utilize_search_in_a_registry.yaml)
* [Push an image to a registry.](data/2_Image_creation_management_registry/push_an_image_to_a_registry.yaml)
* [Sign an image in a registry.](data/2_Image_creation_management_registry/sign_an_image_in_a_registry.yaml)
* Pull and delete images from a registry.

### Domain 3: Installation and Configuration (15% of exam)

* [Describe sizing requirements for installation.](data/3_installation_and_configuration/describe_sizing_requirements_for_installation.yaml)
* Describe and demonstrate the setup of repo, selection of a storage driver, and installation of the Docker engine on multiple platforms.
* Describe and demonstrate configuration of logging drivers (splunk, journald, etc.).
* Describe and demonstrate how to set up swarm, configure managers, add nodes, and setup the backup schedule.
* Describe and demonstrate how to create and manage user and teams.
* [Describe and demonstrate how to configure the Docker daemon to start on boot.](data/3_installation_and_configuration/describe_demonstrate_how_configure_docker_daemon_start_boot.yaml)
* Describe and demonstrate how to use certificate-based client-server authentication to ensure a Docker daemon has the rights to access images on a registry.
* Describe the use of namespaces, cgroups, and certificate configuration.
* Describe and interpret errors to troubleshoot installation issues without assistance.
* Describe and demonstrate the steps to deploy the Docker engine, UCP, and DTR on AWS and on-premises in an HA configuration.
* Describe and demonstrate how to configure backups for UCP and DTR.

### Domain 4: Networking (15% of exam)

* Describe the Container Network Model and how it interfaces with the Docker engine and network and IPAM drivers.
* [Describe the different types and use cases for the built-in network drivers.](data/4_Networking/describe_different_types_use_cases_built_in_network_drivers.yaml)
* Describe the types of traffic that flow between the Docker engine, registry and UCP controllers.
* Describe and demonstrate how to create a Docker bridge network for developers to use for their containers.
* [Describe and demonstrate how to publish a port so that an application is accessible externally.](data/4_Networking/describe_demonstrate_publish_port_application_accessible_externally.yaml)
* Identify which IP and port a container is externally accessible on.
* [Compare and contrast “host” and “ingress” publishing modes.](data/4_Networking/compare_contrats_host_ingress_publishing_modes.yaml)
* Describe and demonstrate how to configure Docker to use external DNS.
* Describe and demonstrate how to use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load balancing with Docker EE).
* Understand and describe the types of traffic that flow between the Docker engine, registry, and UCP controllers
* Describe and demonstrate how to deploy a service on a Docker overlay network.
* Describe and demonstrate how to troubleshoot container and engine logs to resolve connectivity issues between containers.
* Describe how to route traffic to Kubernetes pods using ClusterIP and NodePort services.
* [Describe the Kubertnetes’ container network model.](data/4_Networking/describe_kubernetes_container_network_model.yaml)

### Domain 5: Security (15% of exam)

* [Describe security administration and tasks.](data/5_Security/describe_security_administration_tasks.yaml)
* [Describe the process of signing an image.](data/5_Security/describe_process_signing_image.yaml)
* Describe default engine security.
* [Describe swarm default security.](data/5_Security/swarm_default_security.yaml)
* [Describe MTLS.](data/5_Security/describe_mtls.yaml)
* Describe identity roles.
* [Compare and contrast UCP workers and managers.](data/5_Security/compare_contrast_ucp_workers_managers.yaml)
* Describe the process to use external certificates with UCP and DTR.
* Describe and demonstrate that an image passes a security scan.
* [Describe and demonstrate how to enable Docker Content Trust.](data/5_Security/describe_demonstrate_how_enable_docker_content_trust.yaml)
* Describe and demonstrate how to configure RBAC with UCP.
* Describe and demonstrate how to integrate UCP with LDAP/AD.
* Describe and demonstrate how to create UCP client bundles.

### Domain 6: Storage and Volumes (10% of exam)

* Identify the correct graph drivers to uses with various operating systems.
* [Describe and demonstrate how to configure devicemapper.](data/6_storage_and_volumes/describe_demonstrate_how_to_configure_devicemapper.yaml)
* Compare and contrast object and block storage and when they should be used.
* Describe how an application is composed of layers and where these layers reside on the filesystem.
* Describe the use of volumes are used with Docker for persistent storage.
* Identify the steps to take to clean up unused images on a filesystem and DTR.
* Describe and demonstrate how storage can be used across cluster nodes.
* Describe how to provision persistent storage to a Kubernetes pod using persistentVolumes.
* Describe the relationship between container storage interface drivers, storageClass, persistentVolumeClaim and volume objects in Kubernetes.

