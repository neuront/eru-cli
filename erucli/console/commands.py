# coding: utf-8

from erucli.console.app import (register_app_version, set_app_env, list_app_env_content,
        list_app_containers, deploy_private_container, deploy_public_container,
        build_image, build_log, remove_containers, offline_version, list_app_env_names,
        container_log, alloc_resource, update_version)
from erucli.console.entity import (create_group, create_pod, create_host,
        assign_pod_to_group, assign_host_to_group)

commands = {
    'app:register': register_app_version,
    'app:setenv': set_app_env,
    'app:getenv': list_app_env_content,
    'app:listenv': list_app_env_names,
    'app:dpri': deploy_private_container,
    'app:dpub': deploy_public_container,
    'app:build': build_image,
    'app:listcontainer': list_app_containers,
    'app:rmcontainer': remove_containers,
    'app:offline': offline_version,
    'app:update': update_version,
    'app:allocresource': alloc_resource,

    'group:create': create_group,
    'pod:create':create_pod,
    'pod:assign': assign_pod_to_group,
    'host:create': create_host,
    'host:assign': assign_host_to_group,

    'log:task': build_log,

    'log:container': container_log,
}

