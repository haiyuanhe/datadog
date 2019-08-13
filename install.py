# coding: utf-8
import os, sys
import yaml
from os import path
from optparse import OptionParser

# salt install need
import getpass
from string import Template


def parse_cmdline(argv):
    # get arguments
    parser = OptionParser(description='Setup module config')
    parser.add_option('--default_config', dest='default_config',
                      help='Default agent config e.g: uuid , ip, hostname ')

    (options, args) = parser.parse_args(args=argv[1:])
    return options, args


def init_manifest(options):
    if options.default_config is None:
        if ROOT_PATH is None:
            print "Default config path not be none, please use  python install.py --help "
            sys.exit(1)
        else:
            default_config_path = path.join(ROOT_PATH, "config.yaml")
    else:
        default_config_path = options.default_config

    manifest_config = path.join(MODULE_PATH, "manifest.yaml")
    with open(default_config_path, "r") as f:
        default = yaml.safe_load(f)
    with open(manifest_config) as f:
        manifest_content = yaml.safe_load(f.read()) or {}
        manifest_content.update(default)
        result = yaml.dump(manifest_content, default_flow_style=False)

    with open(manifest_config, 'w') as f:
        f.write(result)

    return default


def init_datadog_config(config):
    template = path.join(MODULE_PATH, ".datadog_template.conf")
    config_path = path.join(MODULE_PATH ,"agent", "datadog.conf")
    with open(template, "r") as f:
        config['module_path'] = MODULE_PATH
        config['hostname'] = config.get('one')['hostname']
        config['uuid'] = config.get('one')['uuid']
        config['api_key'] = config.get('one')['api_key']
        config['ip'] = config.get('one')['ip']

        with open(config_path, "w") as fp:
            fp.write(Template(f.read()).safe_substitute(config))


if __name__ == '__main__':
    MODULE_PATH = os.getcwd()
    ROOT_PATH = os.getenv("ROOT_PATH")
    options, args = parse_cmdline(sys.argv)

    manifest = init_manifest(options)
    init_datadog_config(manifest)
