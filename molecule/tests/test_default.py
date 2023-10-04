import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ca_bundle(host):
    f = host.file('/etc/pki/ca-trust/source/anchors/vault_ca_bundle.pem')
    assert f.exists
    assert f.uid == 0
    assert f.gid == 0
    assert f.mode == 0o644


def test_keymat_targets(host):
    f = host.file('/root/.bootstrap_pki/bootstrap-ansible.dev.rii.io.key')
    assert f.exists
    assert f.uid == 0
    assert f.gid == 0
    assert f.mode == 0o600

    f = host.file('/root/.bootstrap_pki/bootstrap-ansible.dev.rii.io.pem')
    assert f.exists
    assert f.uid == 0
    assert f.gid == 0
    assert f.mode == 0o644

    f = host.file('/root/.bootstrap_pki/vault_ca_bundle.pem')
    assert f.exists
    assert f.uid == 0
    assert f.gid == 0
    assert f.mode == 0o644


def test_bs_install_target(host):
    f = host.file('/bootstrap-pki')
    assert not f.exists


def test_bs_srl(host):
    f = host.file('/root/.srl')
    assert not f.exists
