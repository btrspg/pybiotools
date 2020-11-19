# AUTOGENERATED! DO NOT EDIT! File to edit: 10_rnasamba.ipynb (unless otherwise specified).

__all__ = ['Rnasamba']

# Cell

from ..base import Base,modify_cmd

# Cell

class Rnasamba(Base):
    def __init__(self, software, fd):
        super(Rnasamba, self).__init__(software)
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
    def cmd_training_model(self, output_file, coding_file, noncoding_file):
        '''

        :param output_file:
        :param coding_file:
        :param noncoding_file:
        :return:
        '''


        return r'''
{software} {train_para} \
            {output_file} \
            {coding_file} \
            {noncoding_file}
            '''.format(
                train_para=self._default['train'],
                software=self._software,
                **locals()
            )

    @modify_cmd
    def cmd_classify(self,protein_fasta,output_file,fasta_file,weights):
        return r'''
{software} {classify_para} \
            -p {protein_fasta} \
            {output_file} \
            {fasta_file} \
            {weights}
        '''.format(
            software=self._software,
            classify_para=self._default['classify'],
            **locals()
        )

    def __repr__(self):
        return 'rnasamba:' + self._software

    def __str__(self):
        return 'RNAsamba is a tool for computing the coding potential of RNA ' \
               'sequences using a neural network classification model. ' \
               'It can be used to identify mRNAs and lncRNAs without relying ' \
               'on database searches. '