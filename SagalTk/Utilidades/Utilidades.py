#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Utilidades (Utilidades de Sagal in spanish).

    Copyright © 2019 Ismael Belisario

    This file is part of Sagal.

    Sagal is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Sagal is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Sagal.  If not, see <https://www.gnu.org/licenses/>.

    
       Conjunto de micro aplicaciones con el fin de servir
    de soporte Sagal (Directamente a diferencia de Micrapps).
"""

from os.path import basename
from sys import argv, stderr
import argparse
import re

class Sarguer(argparse.ArgumentError):
    """
    Nombre
        Sarguer (Sagal ArgumentError) 

    """

    def __init__(self, argument, message):
        super().__init__(argument, message)

    def __str__(self):
        #format = ""
        if self.argument_name is None:
            format = '%(message)s'
        else:
            format = 'Argumento %(argument_name)s: %(message)s.'
        
        return format % dict(message=self.message,
                             argument_name=self.argument_name)

class Sahelfor(argparse.HelpFormatter):
    """
    Nombre
           Sahelfor (Sagal HelpFormatter)
    
    description
           HelpFormatter de Sagal
    """
    def __init__(self, prog, indent_increment=2,
                 max_help_position=24, width=None):

        super().__init__(prog, indent_increment,
                         max_help_position, width)
    
    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = ('Uso: ')

        # if usage is specified, use that
        if usage is not None:
            usage = usage % dict(prog=self._prog)

        # if no optionals or positionals are available, usage is just prog
        elif usage is None and not actions:
            usage = '%(prog)s' % dict(prog=self._prog)

        # if optionals and positionals are available, calculate usage
        elif usage is None:
            prog = '%(prog)s' % dict(prog=self._prog)

            # split optionals from positionals
            optionals = []
            positionals = []
            for action in actions:
                if action.option_strings:
                    optionals.append(action)
                else:
                    positionals.append(action)

            # build full usage string
            format = self._format_actions_usage
            action_usage = format(optionals + positionals, groups)
            usage = ' '.join([s for s in [prog, action_usage] if s])

            # wrap the usage parts if it's too long
            text_width = self._width - self._current_indent
            if len(prefix) + len(usage) > text_width:

                # break usage into wrappable parts
                part_regexp = (
                    r'\(.*?\)+(?=\s|$)|'
                    r'\[.*?\]+(?=\s|$)|'
                    r'\S+'
                )
                opt_usage = format(optionals, groups)
                pos_usage = format(positionals, groups)
                opt_parts = re.findall(part_regexp, opt_usage)
                pos_parts = re.findall(part_regexp, pos_usage)
                assert ' '.join(opt_parts) == opt_usage
                assert ' '.join(pos_parts) == pos_usage

                # helper for wrapping lines
                def get_lines(parts, indent, prefix=None):
                    lines = []
                    line = []
                    if prefix is not None:
                        line_len = len(prefix) - 1
                    else:
                        line_len = len(indent) - 1
                    for part in parts:
                        if line_len + 1 + len(part) > text_width and line:
                            lines.append(indent + ' '.join(line))
                            line = []
                            line_len = len(indent) - 1
                        line.append(part)
                        line_len += len(part) + 1
                    if line:
                        lines.append(indent + ' '.join(line))
                    if prefix is not None:
                        lines[0] = lines[0][len(indent):]
                    return lines

                # if prog is short, follow it with optionals or positionals
                if len(prefix) + len(prog) <= 0.75 * text_width:
                    indent = ' ' * (len(prefix) + len(prog) + 1)
                    if opt_parts:
                        lines = get_lines([prog] + opt_parts, indent, prefix)
                        lines.extend(get_lines(pos_parts, indent))
                    elif pos_parts:
                        lines = get_lines([prog] + pos_parts, indent, prefix)
                    else:
                        lines = [prog]

                # if prog is long, put it on its own line
                else:
                    indent = ' ' * len(prefix)
                    parts = opt_parts + pos_parts
                    lines = get_lines(parts, indent)
                    if len(lines) > 1:
                        lines = []
                        lines.extend(get_lines(opt_parts, indent))
                        lines.extend(get_lines(pos_parts, indent))
                    lines = [prog] + lines

                # join lines into usage
                usage = '\n'.join(lines)

        # prefix with 'usage:'
        return '%s\n\n%s%s\n\n' % (" " * 20 + "Sagal", prefix, usage)
    
    


class Sagarmen(argparse.ArgumentParser):
    
    """ 
    Nombre
            Sagarmen (Sagal ArgumentParser)
    
    Descripción 
            ArgumentParser de Sagal (sin más)
    """
    
    def __init__(self, prog=None, usage=None, description=None,
                 epilog=None, parents=[],
                 formatter_class=Sahelfor, prefix_chars='-',
                 fromfile_prefix_chars=None, 
                 argument_default=None, conflict_handler='error',
                 add_help=True, allow_abbrev=True):
        
        superinit = super(argparse.ArgumentParser, self).__init__
        superinit(description=description,
                  prefix_chars=prefix_chars,
                  argument_default=argument_default,
                  conflict_handler=conflict_handler)

        # default setting for prog
        if prog is None:
            prog = basename(argv[0])

        self.prog = prog
        self.usage = usage
        self.epilog = epilog
        self.formatter_class = formatter_class
        self.fromfile_prefix_chars = fromfile_prefix_chars
        self.add_help = add_help
        self.allow_abbrev = allow_abbrev

        add_group = self.add_argument_group
        self._positionals = add_group(('Argumentos pocisionales'))
        self._optionals = add_group(('Argumentos opcionales'))
        self._subparsers = None

        # register types
        def identity(string):
            return string
        self.register('type', None, identity)

        # add help argument if necessary
        # (using explicit default to override global argument_default)
        default_prefix = '-' if '-' in prefix_chars else prefix_chars[0]
        if self.add_help:
            self.add_argument(
                default_prefix+'a', default_prefix*2+'ayuda',
                action='help', default=argparse.SUPPRESS,
                help=('Mostrar este mensaje y salir.'))

        # add parent arguments and defaults
        for parent in parents:
            self._add_container_actions(parent)
            try:
                defaults = parent._defaults
            except AttributeError:
                pass
            else:
                self._defaults.update(defaults)

    def parse_args(self, args=None, namespace=None):
            args, argv = self.parse_known_args(args, namespace)
            if argv:
                msg = ('No se recononoce el argumento: %s.')
                self.error(msg % ' '.join(argv))
            return args
    
    def _match_argument(self, action, arg_strings_pattern):
        # match the pattern for this action to the arg strings
        nargs_pattern = self._get_nargs_pattern(action)
        match = re.match(nargs_pattern, arg_strings_pattern)

        # raise an exception if we weren't able to find a match
        if match is None:
            
            nargs_errors = {
                None: ('Se esperaba un argumento'),
                argparse.OPTIONAL: ('expected at most one argument'),
                argparse.ONE_OR_MORE: ('expected at least one argument'),
            }
            default = argparse.ngettext('expected %s argument',
                               'expected %s arguments',
                               action.nargs) % action.nargs

            msg = nargs_errors.get(action.nargs, default)
            raise Sarguer(action, msg)

        # return the number of arguments matched
        return len(match.group(1))
    
    
    def error(self, message):
        """error(mensaje: texto)

        Imprime un uso del mensaje lo imcorpora a stderr y salir.

        If you override this in a subclass, it should not return -- it
        should either exit or raise an exception.
        """
        self.print_usage(stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(2, ('%(prog)s: Error: %(message)s\n') % args)