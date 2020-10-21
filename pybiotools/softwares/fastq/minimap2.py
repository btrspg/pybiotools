# AUTOGENERATED! DO NOT EDIT! File to edit: 12_minimap2.ipynb (unless otherwise specified).

__all__ = ['Minimap2']

# Cell

from ..base import Base, modify_cmd



# Cell

class Minimap2(Base):
    def __init__(self, software, fd):
        super(Minimap2, self).__init__(software)
        self._default = fd

    @modify_cmd
    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software} --version'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_splice_align(self,reference,fastq,samtools,samtools_idx,outbam):

        return r'''
{software} {splice_align} -a {reference} {fastq} | {samtools_sam2bam} | {samtools_sort}
{samtools_index}
        '''.format(
            software=self._software,
            splice_align=self._default['splice_align'],
            samtools_sam2bam=samtools.cmd_sam2bam(samtools_idx, '-', bamfile=None),
            samtools_sort=samtools.cmd_sort('-', sortbam=outbam),
            samtools_index=samtools.cmd_index(outbam),
            **locals()
        )

    @modify_cmd
    def cmd_nonsplice_align(self,reference,fastq,samtools,samtools_idx,outbam):

        return r'''
{software} {nonsplice_align} -a {reference} {fastq} | {samtools_sam2bam} | {samtools_sort}
{samtools_index}
        '''.format(
            software=self._software,
            nonsplice_align=self._default['nonsplice_align'],
            samtools_sam2bam=samtools.cmd_sam2bam(samtools_idx, '-', bamfile=None),
            samtools_sort=samtools.cmd_sort('-', sortbam=outbam),
            samtools_index=samtools.cmd_index(outbam),
            **locals()
        )

    def __repr__(self):
        return 'minimap2:' + self._software

    def __str__(self):
        return 'A versatile pairwise aligner for genomic and spliced nucleotide sequences'