#!/usr/bin/env python3


import sys,re,os
import pathlib

import ugrmgm.util

USER_INFO_USER_FILE="/etc/passwd"
USER_INFO_PASS_FILE="/etc/shadow"
GROUP_INFO_FILE="/etc/group"



class UserAction( object ):
    """
    User class implementes actions that can be taken for a selected user
    """

    def __init__(self, username, **opt ):
        self.__debug = ugrmgm.util.boolify( opt.get( "debug", False ) )
        self.__username = username
        self.__info =  None
        
        self.__action_lock = ugrmgm.util.boolify( opt.get( "lock", False ) )
        self.__action_unlock = ugrmgm.util.boolify( opt.get( "unlock", False ) )
        self.__action_expire = opt.get( "expire", None )

        self.__action_mkhome = ugrmgm.util.boolify( opt.get( "create_home", False ) )
        self.__action_uid = opt.get( "uid", None )
        self.__action_group = opt.get( "group", None )
        self.__action_groups = opt.get( "groups", list() )
        self.__action_shell = opt.get( "shell", "/bin/bash" )

    def __load_info( self ):
        self.__info = ugrmgm.info.UserInfo( self.__username, debug=self.__debug )

    def __create_user( self ):
        pass
    
    def __remove_user( self ):
        pass

    def __modify_user( self ):
        pass


    def __exec_expire_account( self, exp ):
        pass

    def __exec_lock_account( self ):
        pass
    
    def __exec_unlock_account( self ):
        pass


class UserInfo( object ):
    """
    UserInfo class contains information about the selected user
    """
    def __init__( self, username, **opt ):
        self.__debug = ugrmgm.util.boolify( opt.get( "debug", False ) )
        self.__username = username
        self.__info =  None
    
        self.__user_name = username
        self.__user_uid = None
        self.__user_gid = None
        self.__user_comment = None
        self.__user_shell = None
        self.__user_home = None
        self.__user_x = None    
        self.__user_groups = None
        
        self.__shadow_locked = None
        self.__shadow_pasword = None
        self.__shadow_last_change = None
        self.__shadow_min_password_age = None
        self.__shadow_max_pasword_age = None
        self.__shadow_pasword_warn = None
        self.__shadow_pasword_inact = None
        self.__shadow_pasword_exiration = None
        self.__shadow_extra = None

    
class UserList( object ):
    """
    UserList manages a list of users, mainly information about existsing  users
    """
    
    
class Group( object ):
    def __init__(self, groupname, **opt ):
        pass
    
class GroupInfo( object ):
    def __init__(self, groupname, **opt ):
        pass
    
class GroupList( object ):
    def __init__(self, groupname, **opt ):
        pass