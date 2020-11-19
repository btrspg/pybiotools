# AUTOGENERATED! DO NOT EDIT! File to edit: 08_inhouse_rscript.ipynb (unless otherwise specified).

__all__ = ['Inhouerscript']

# Cell

import os
from ..base import Base, modify_cmd


# Cell


class Inhouerscript(Base):
    def __init__(self, software, fd):
        super(Inhouerscript, self).__init__(software)
        self._default = fd
        if '/' in software:
            bin = os.path.dirname(software) + '/'
        else:
            bin = ''
        self._deseq2 = bin + 'deseq2.R'



    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software}'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_deg_deseq2(self, count,clinical,control,prefix):
        '''
        '''
        return r'''
{software} {count} \
            {clinical} \
            {control} \
            {prefix}
        '''.format(
            software=self._deseq2,
            **locals()
        )

    def __repr__(self):
        return 'inhouserscript:' + self._software

    def __str__(self):
        return '''
In-house Rscripts rep, https://github.com/btrspg/bioinfo-rscripts
        '''