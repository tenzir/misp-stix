#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import Mapping
from .stix2_mapping import STIX2Mapping


class InternalSTIX2Mapping(STIX2Mapping):
    def __init__(self):
        super().__init__()
        self._declare_mapping()
        attributes_mapping = {
            'AS': '_attribute_from_AS',
            'attachment': '_attribute_from_attachment',
            'domain': '_attribute_from_domain',
            'domain|ip': '_attribute_from_domain_ip',
            'email': '_attribute_from_email',
            'email-attachment': '_attribute_from_email_attachment',
            'email-body': '_attribute_from_email_body',
            'email-dst': '_attribute_from_email_destination',
            'email-header': '_attribute_from_email_header',
            'email-reply-to': '_attribute_from_email_reply_to',
            'email-src': '_attribute_from_email_source',
            'email-subject': '_attribute_from_email_subject',
            'email-x-mailer': '_attribute_from_email_x_mailer',
            'filename': '_attribute_from_filename',
            'hostname': '_attribute_from_domain',
            'hostname|port': '_attribute_from_hostname_port',
            'http-method': '_attribute_from_http_method',
            'mac-address': '_attribute_from_mac_address',
            'malware-sample': '_attribute_from_malware_sample',
            'mutex': '_attribute_from_mutex',
            'port': '_attribute_from_port',
            'regkey': '_attribute_from_regkey',
            'regkey|value': '_attribute_from_regkey_value',
            'size-in-bytes': '_attribute_from_size_in_bytes',
            'user-agent': '_attribute_from_user_agent',
            'vulnerability': '_parse_vulnerability_attribute'
        }
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'md5',
                    'sha1',
                    'sha224',
                    'sha256',
                    'sha384',
                    'sha512',
                    'sha512/224',
                    'sha512/256',
                    'sha3-224',
                    'sha3-256',
                    'sha3-384',
                    'sha3-512',
                    'ssdeep',
                    'tlsh'
                ),
                '_attribute_from_hash'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'filename|md5',
                    'filename|sha1',
                    'filename|sha224',
                    'filename|sha256',
                    'filename|sha384',
                    'filename|sha512',
                    'filename|sha512/224',
                    'filename|sha512/256',
                    'filename|sha3-224',
                    'filename|sha3-256',
                    'filename|sha3-384',
                    'filename|sha3-512',
                    'filename|ssdeep',
                    'filename|tlsh'
                ),
                '_attribute_from_filename_hash'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'ip-src',
                    'ip-dst'
                ),
                '_attribute_from_ip'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'ip-src|port',
                    'ip-dst|port'
                ),
                '_attribute_from_ip_port'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'uri',
                    'url',
                    'link'
                ),
                '_attribute_from_url'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'x509-fingerprint-md5',
                    'x509-fingerprint-sha1',
                    'x509-fingerprint-sha256'
                ),
                '_attribute_from_x509_fingerprint'
            )
        )
        attributes_mapping.update(
            dict.fromkeys(
                (
                    'sigma',
                    'snort',
                    'yara'
                ),
                '_attribute_from_patterning_language'
            )
        )
        self.__attributes_mapping = Mapping(**attributes_mapping)
        galaxies_mapping = {'branded-vulnerability': '_galaxy_from_attack_pattern'}
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'mitre-attack-pattern',
                    'mitre-enterprise-attack-attack-pattern',
                    'mitre-mobile-attack-attack-pattern',
                    'mitre-pre-attack-attack-pattern'
                ),
                '_galaxy_from_attack_pattern'
            )
        )
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'mitre-course-of-action',
                    'mitre-enterprise-attack-course-of-action',
                    'mitre-mobile-attack-course-of-action'
                ),
                '_galaxy_from_course_of_action'
            )
        )
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'mitre-enterprise-attack-intrusion-set',
                    'mitre-intrusion-set',
                    'mitre-mobile-attack-intrusion-set',
                    'mitre-pre-attack-intrusion-set'
                ),
                '_galaxy_from_intrusion_set'
            )
        )
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'android',
                    'banker',
                    'stealer',
                    'backdoor',
                    'ransomware',
                    'mitre-malware',
                    'malpedia',
                    'mitre-enterprise-attack-malware',
                    'mitre-mobile-attack-malware'
                ),
                '_galaxy_from_malware'
            )
        ),
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'threat-actor',
                    'microsoft-activity-group'
                ),
                '_galaxy_from_threat_actor'
            )
        )
        galaxies_mapping.update(
            dict.fromkeys(
                (
                    'botnet',
                    'rat',
                    'exploit-kit',
                    'tds',
                    'tool',
                    'mitre-tool',
                    'mitre-enterprise-attack-tool',
                    'mitre-mobile-attack-tool'
                ),
                '_galaxy_from_tool'
            )
        )
        self.__galaxies_mapping = Mapping(**galaxies_mapping)
        objects_mapping = {
            'android-app': '_object_from_android_app',
            'asn': '_object_from_asn',
            'attack-pattern': '_parse_attack_pattern_object',
            'course-of-action': '_parse_course_of_action_object',
            'cpe-asset': '_object_from_cpe_asset',
            'credential': '_object_from_credential',
            'domain-ip': '_object_from_domain_ip',
            'email': '_object_from_email',
            'employee': '_parse_employee_object',
            'facebook-account': '_object_from_account',
            'file': '_object_from_file',
            'image': '_object_from_image',
            'ip-port': '_object_from_ip_port',
            'legal-entity': '_parse_legal_entity_object',
            'lnk': '_object_from_lnk',
            'mutex': '_object_from_mutex',
            'network-connection': '_object_from_network_connection',
            'network-socket': '_object_from_network_socket',
            'process': '_object_from_process',
            'registry-key': '_object_from_registry_key',
            'url': '_object_from_url',
            'vulnerability': '_parse_vulnerability_object',
            'x509': '_object_from_x509'
        }
        objects_mapping.update(
            dict.fromkeys(
                (
                    'github-user',
                    'gitlab-user',
                    'parler-account',
                    'reddit-account',
                    'telegram-account',
                    'twitter-account',
                    'user-account'
                ),
                '_object_from_account'
            )
        )
        self.__objects_mapping = Mapping(**objects_mapping)

        # STIX TO MISP OBJECTS MAPPING
        self.__attack_pattern_object_mapping = Mapping(
            description = {'type': 'text', 'object_relation': 'summary'},
            name = {'type': 'text', 'object_relation': 'name'},
            x_misp_prerequisites = {'type': 'text', 'object_relation': 'prerequisites'},
            x_misp_related_weakness = {'type': 'weakness', 'object_relation': 'related-weakness'},
            x_misp_solutions = {'type': 'text', 'object_relation': 'solutions'}
        )
        self.__course_of_action_object_mapping = Mapping(
            name = {'type': 'text', 'object_relation': 'name'},
            description = {'type': 'text', 'object_relation': 'description'},
            x_misp_cost = {'type': 'text', 'object_relation': 'cost'},
            x_misp_efficacy = {'type': 'text', 'object_relation': 'efficacy'},
            x_misp_impact = {'type': 'text', 'object_relation': 'impact'},
            x_misp_objective = {'type': 'text', 'object_relation': 'objective'},
            x_misp_stage = {'type': 'text', 'object_relation': 'stage'},
            x_misp_type = {'type': 'text', 'object_relation': 'type'}
        )
        employee_type = {'type': 'text', 'object_relation': 'employee-type'}
        self.__employee_object_mapping = Mapping(
            name = {'type': 'full-name', 'object_relation': 'full-name'},
            description = {'type': 'text', 'object_relation': 'text'},
            roles = employee_type,
            x_misp_business_unit = {'type': 'target-org', 'object_relation': 'business_unit'},
            x_misp_employee_type = employee_type,
            x_misp_first_name = {'type': 'first-name', 'object_relation': 'first-name'},
            x_misp_last_name = {'type': 'last-name', 'object_relation': 'last-name'},
            x_misp_primary_asset = {'type': 'target-machine', 'object_relation': 'primary-asset'},
            x_misp_userid = {'type': 'target-user', 'object_relation': 'userid'}
        )
        self.__legal_entity_contact_information_mapping = Mapping(
            **{
                'phone-number': {'type': 'phone-number'},
                'website': {'type': 'link'}
            }
        )
        self.__legal_entity_object_mapping = Mapping(
            name = {'type': 'text', 'object_relation': 'name'},
            description = {'type': 'text', 'object_relation': 'text'},
            sectors = {'type': 'text', 'object_relation': 'business'},
            x_misp_commercial_name = {'type': 'text', 'object_relation': 'commercial-name'},
            x_misp_legal_form = {'type': 'text', 'object_relation': 'legal-form'},
            x_misp_registration_number = {'type': 'text', 'object_relation': 'registration-number'}
        )

    @property
    def attack_pattern_object_mapping(self) -> dict:
        return self.__attack_pattern_object_mapping

    @property
    def attributes_mapping(self) -> dict:
        return self.__attributes_mapping

    @property
    def course_of_action_object_mapping(self) -> dict:
        return self.__course_of_action_object_mapping

    @property
    def employee_object_mapping(self) -> dict:
        return self.__employee_object_mapping

    @property
    def galaxies_mapping(self) -> dict:
        return self.__galaxies_mapping

    @property
    def legal_entity_contact_information_mapping(self) -> dict:
        return self.__legal_entity_contact_information_mapping

    @property
    def legal_entity_object_mapping(self) -> dict:
        return self.__legal_entity_object_mapping

    @property
    def objects_mapping(self) -> dict:
        return self.__objects_mapping