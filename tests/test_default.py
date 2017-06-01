import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_consul_is_installed(File):
    consul = File("/usr/local/bin/consul")
    assert consul.exists
    assert not consul.is_directory
