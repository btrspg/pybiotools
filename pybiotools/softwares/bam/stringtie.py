# AUTOGENERATED! DO NOT EDIT! File to edit: 06_stringtie.ipynb (unless otherwise specified).

__all__ = ['Stringtie']

# Cell

from ..base import Base, modify_cmd

# Cell

class Stringtie(Base):
    def __init__(self, software, fd):
        super(Stringtie, self).__init__(software)
        self._default = fd

    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software} --version'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_assemble_transcript(self, bams, outgtf, abundance,annogtf):
        '''
        :param bams:
        :param outgtf:
        :param abundance:
        :param annogtf:
        :return:
        '''
        return r'''
{stringtie} {assemble_transcript} \
            -o {outgtf} \
            -G {annogtf} \
            -A {abundance} \
            {bams}
        '''.format(
            stringtie=self._software,
            bams=bams if isinstance(bams, str) else ' '.join(bams),
            assemble_transcript=self._default['assemble_transcript'],
            outgtf=outgtf,
            annogtf=annogtf,
            abundance=abundance

        )

    @modify_cmd
    def cmd_merge_gtf(self, gtfs, output, tag=None):
        '''
        :param gtfs:
        :param output:
        :param tag:
        :param nt:
        :return:
        '''
        if tag is None:
            tag = ' -l MERGE'
        else:
            tag = ' -l ' + tag
        return r'''
{stringtie} {merge_paras} {tag} \
    -o {output} \
    {gtfs}
    '''.format(
            stringtie=self._software,
            gtfs=gtfs if isinstance(gtfs, str) else ' '.join(gtfs),
            merge_paras=self._default['merge'],
            output=output,
            tag=tag

        )

    def __repr__(self):
        return 'stringtie:' + self._software

    def __str__(self):
        return 'Transcript assembly and quantification for RNA-Seq'
