from mountaintools import client as mt
import kachery as ka

mt.configDownloadFrom('spikeforest.public')
ka.set_config(
    download=True,
    upload=True
)

X = mt.loadObject(path='sha1://04a29bf145a2833533527262f5f30104bcc53679/analysis.json')
ka.store_object(X, basename='analysis.json')

X = ka.load_object('sha1://04a29bf145a2833533527262f5f30104bcc53679/analysis.json')

studies_to_include = ['paired_kampff']
fnames = ['geom.csv', 'params.json', 'raw.mda', 'firings_true.mda']
# fnames = ['geom.csv', 'params.json']
for studyset in X['StudySets']:
    print('STUDYSET: {}'.format(studyset['name']))
    for study in studyset['studies']:
        study_name = study['name']
        print('STUDY: {}'.format(study_name))
        if study_name in studies_to_include:
            for recording in study['recordings']:
                recname = recording['name']
                recdir = recording['directory']
                print(recname, recdir)
                for fname in fnames:
                    ff = mt.realizeFile(path=recdir + '/' + fname)
                    ka.store_file(ff)
