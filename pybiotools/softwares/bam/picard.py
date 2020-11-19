# AUTOGENERATED! DO NOT EDIT! File to edit: 15_picard.ipynb (unless otherwise specified).

__all__ = ['Picard']

# Cell

from ..base import Base, modify_cmd


# Cell

class Picard(Base):
    def __init__(self, software, fd):
        super(Picard, self).__init__(software)
        self._default = fd

    def cmd_version(self):
        return 'echo {repr};echo NOVERSION '.format(
            repr=self.__repr__()
        )


    @modify_cmd
    def cmd_mark_duplicates(self, bam_file, marked_bam, qc_prefix, tmp):
        '''
        :param bam_file:
        :param marked_bam:
        :param qc_prefix:
        :param tmp:
        :return:
        '''
        return r'''
{software} -Djava.io.tmpdir={tmp} {markdup_para} \
          I={bam_file} \
          O={marked_bam} \
          M={qc_prefix}.marked_dup_metrics.txt
{software} -Djava.io.tmpdir={tmp} {bbi_para} \
          I={marked_bam}
            '''.format(
            tmp=tmp,
            markdup_para=self._default['markdup'],
            bbi_para=self._default['buildbamindex'],
            software=self._software,
            bam_file=bam_file,
            qc_prefix=qc_prefix,
            marked_bam=marked_bam
        )

    def __repr__(self):
        return 'picard:' + self._software

    def __str__(self):
        return 'A set of command line tools (in Java) for manipulating high-throughput ' \
               'sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF'