#!/usr/bin/env python3

import pathlib
import re,os,re
import datetime
import json
import random, string
from pathlib import Path
from pprint import pprint

from ugrmgm.checksum import file_hash
from ugrmgm.checksum import data_hash


BOOLIFY_TRUE=( True, "True", "Yes", "yes", 1 )
BOOLIFY_FALSE=( False, "False", "No", "no", 0 )

def boolify( s ):
    if s in BOOLIFY_TRUE:
        return True
    elif s in BOOLIFY_FALSE:
        return False
    else:
        raise AttributeError("Bad boolish value" )
        
    
def read_env( key ):
    if key not in os.environ:
        return None
    return os.environ.get( key )


################################################################################
## Local file operaitons
################################################################################

def _read_text( filename ):
    result = list()
    try:
        fd = open( filename, "r" )
        for line in fd.readlines():
            result.append( line.lstrip().rstrip() )
        return result
    except Exception as e:
        print("ERROR Reading %s: %s" % ( filename, e ))

    return result

def _read_json( filename ):
    return json.loads( "\n".join( _read_text( filename ) ) )

def load_file( filename ):
    filesplit = re.split( r"\.", filename )
    if filesplit[-1] in ( "json" ):
        return _read_json( filename )
    else:
        return _read_text( filename )


def _write_json( filename, data ):
    return _write_text( filename, json.dumps( data, indent=2, sort_keys=True ) )

def _write_text( filename, data ):
    fd = open( filename, "w" )
    fd.write( str( data ) )
    fd.close()

def write_file( filename, data ):
    filesplit = re.split( "\.", filename )
    if filesplit[-1] in ( "json" ):
        return _write_json( filename, data )
    else:
        return _write_text( filename, data )

def semi_crunch( string ):
    return re.split( r"[;]", string )

def read_env( key ):
    if key not in os.environ:
        return None
    return os.environ.get( key )

def rmdir_tree( path ):
    pth = Path( path )
    for sub in pth.iterdir() :
        if sub.is_dir() :
            rmdir_tree(sub)
        else:
            sub.unlink()
    pth.rmdir()

def mk_temp_dir( root="/tmp" ):
    return "%s/crate_%s" % ( root, random_string( 6 ) )


def time_now_raw():
    return datetime.datetime.now()

def time_now_isoformat():
    return time_now_raw().isoformat()

def time_now_string():
    return time_now_raw().strftime( "%Y%m%d_%H%M%S.%f" )

def date_now_string():
    return time_now_raw().strftime( "%Y%m%d" )

def random_string( length=10):
    return ''.join(random.SystemRandom().choice( string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range( length ))

def random_tempdir( rootdir="/tmp", rlen=5, create=False ):
    random_dir = pathlib.Path( "%s/%s" % ( rootdir, random_string( rlen ) ) )
    if create and not random_dir.exists():
        random_dir.mkdir( exist_ok=False, parents=True )
    return random_dir

def dirtree( root, path="", filter=".*" ):
    res = list()

    pref = ""
    rpath = root
    if len( path ) > 0:
       rpath = "%s/%s" % ( root, path )
       pref = "%s/" % ( path )

    for f in [ "%s%s" %( pref, f.name ) for f in Path( rpath ).iterdir() if re.match( filter, f.name ) and f.name not in (".","..", ".git") ]:
       i = Path( "%s/%s" % (root, f ))
       if i.is_dir():
           res += dirtree( root, f, filter )     
       elif i.is_file():
           res.append( f )
    return res

if __name__ == "__main__":
    pass