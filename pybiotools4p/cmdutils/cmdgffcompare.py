# AUTOGENERATED! DO NOT EDIT! File to edit: u02_gffcompare.ipynb (unless otherwise specified).

__all__ = ['gffcompare_multiple_gtf_tracking', 'sample_name_in_tracking']

# Cell

import yaml

# Cell

def gffcompare_multiple_gtf_tracking(tracking_file,outdir,*,names=None,split=True):
    '''
    The tracking file in results of gffcompare -r anno.gtf 1.gtf 2.gtf 3.gtf ...
    Extract transcript list for each sample, which would be used to draw venn diagram

    :param str tracking_file: tracking file
    :param str outdir: output direction
    :param list[str] names: names correspanding to q1,q2... in tracking file
    :param bool split: wheather split different tags in to different files, if not, only consider class_code '=' and other than that.
    '''

    tags = {
        '=':'known'
    }
    new_tag={}
    records= {}
    nt_ot={}
    with open(tracking_file,'r') as tr:
        line = tr.readline()
        while line:
            cells = line.strip().split('\t')
            if split:
                tag = tags.get(cells[3],cells[3])
            else:
                tag = tags.get(cells[3],'unknown')
            new_tag.setdefault(tag,0)
            new_tag[tag]+=1
            tag_name = f'{tag}_{new_tag[tag]}'
            sample_infos = cells[4:]
            nt_ot[tag_name]=' '.join(cells[:3])
            for si in sample_infos:
                if si != '-':
                    name=sample_name_in_tracking(si.split(':')[0],names)
                    records.setdefault(name,{})
                    records[name].setdefault(tag,[])
                    records[name][tag].append(tag_name)

            line=tr.readline()
    for sample in records:
        for t in records[sample]:
            with open(f'{outdir}/{sample}_{t}.txt','w') as out:
                out.write('\n'.join(records[sample][t]))
    with open(f'{outdir}/track_name.yaml','w') as y:
        yaml.dump(nt_ot,y)

def sample_name_in_tracking(q_n,names=None):
    if None is names:
        return q_n
    else:
        return names[int(q_n.replace('q',''))-1]