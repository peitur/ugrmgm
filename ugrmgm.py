#!/usr/bin/env python3

import os, re, sys
import argparse
import pathlib

import ugrmgm


def valid_username( s ):
    if re.match("^[a-z][a-z0-9]+$"):
        return s
    raise argparse.ArgumentTypeError( "Bad username format: %s" % ( s ))

def valid_groupname( s ):
    if re.match("^[a-z][a-z0-9]+$"):
        return s
    raise argparse.ArgumentTypeError( "Bad groupname format: %s" % ( s ))

def valid_configpath( s ):
    if pathlib.Path( s ).exists():
        return s
    raise argparse.ArgumentTypeError( "Bad config file: %s" % ( s ))


if __name__ == "__main__":

    parser = argparse.ArgumentParser( prog='ugrmgm', description="User Group Role management tool", epilog="" )
    parser.add_argument( "--debug", help="Debug  output", default=False )
    parser.add_argument( "-c", "--config", help="Configuration file", default=ugrmgm.DEFAULT_CONFIG, type=valid_configpath )

    sparser = parser.add_subparsers( help="Subcommands", dest="subcommand" )

    parser_create = sparser.add_parser("create", help="Create a user(s)" )

    parser_remove = sparser.add_parser("remove", help="Remove user(s)" )

    parser_modify = sparser.add_parser("modify", help="Modify user" )
    
    parser_validate = sparser.add_parser("validate", help="Validate user" )

    parser_print = sparser.add_parser("print", help="Print  details about user" )
