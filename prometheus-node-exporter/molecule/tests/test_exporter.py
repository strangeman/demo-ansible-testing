import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_node_exporter_installed(host):
    package_node_exporter = host.package('node_exporter')
    assert package_node_exporter.is_installed
    assert package_node_exporter.version.startswith("0.18.1")


def test_is_node_exporter_servive_enabled(host):
    assert host.service("node_exporter").is_running is True
    assert host.service("node_exporter").is_enabled is True
