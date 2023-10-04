rii.pki-bootstrap
=========
Deploys cryptographic materials including keys and certificates for Vault and Consul. Then deploys PKI (Public Key Infrastructure) during system bootstrapping

Requirements
------------

RedHat is required on the target machine.

Role Variables
--------------

* `pki_bs_install_target`: It defines the target directory for installing bootstrapped PKI. It Defaults to: "{{ lookup('env', 'PWD') }}/.bootstrap-pki"
* `pki_bs_rekey_required`: It is used to determine if rekeying (generating new cryptographic keys) is required for the PKI
 It Defaults to: "{{ lookup('env', 'RII_ANSIBLE_VAULT_PKI_BOOTSTRAP') | default(false, true) }}"
* `pki_bs_cluster_name`: This variable specifies the name of the PKI cluster. Defaults to : `vault`
* `management_node`: This variable determines whether the node is a management node. It Defaults to: "{{ not (vagrant_mode | default(false) | bool) }}"
* `pki_bs_srl`: This variable defines the location of the serial file used in PKI operations "{{ lookup('env', 'PWD') }}/.srl"
* `pki_bs_ca_cert`: Specifies the path to the bootstrap CA (Certificate Authority) certificate file."{{ * * * * 
pki_bs_install_target }}/bootstrap-ca.pem"
* `pki_bs_ca_key`: specifies the path to the bootstrap CA private key file. Defaults to:"{{ pki_bs_install_target }}/bootstrap-ca.key"
* `pki_bs_ca_config`: Defines the path to the OpenSSL configuration file used for the bootstrap CA. Defaults to:"{{ role_path }}/files/openssl-bootstrap-ca.cnf"
* `pki_bs_config`: Defines the path to the OpenSSL configuration file used for the bootstrap process. Defaults to: "{{ role_path }}/files/openssl-bootstrap.cnf"
* `pki_bs_cert_name`: Determines the name of the bootstrap certificate. Generate a name based on whether the current host is localhost or in the mgmt group. Defaults to : "{{ (inventory_hostname == 'localhost' or inventory_hostname in groups['mgmt'])
                    | ternary('bootstrap-ansible.' + resolv_domain, ansible_nodename) }}"
`pki_bs_install_target`: : Specifies the directory path where the bootstrapped certificates will be installed. Defaults to :` /bootstrap-pki`
`pki_bs_rekey_required`: It's a boolean flag indicating whether rekeying of certificates is required.Defaults Defaults to: `true`
`resolv_domain`: Used to set the domain for DNS resolution. Defaults to"{{ ansible_domain }}"
`rii_vault_cert_path`:  Specifies the directory path where the Vault certificates will be stored. Defaults to : `/certs`

Dependencies
-----------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: rii.pki-bootstrap

License
-------

RII Proprietary

Author Information
------------------

Research Innovations Inc. (RII)
