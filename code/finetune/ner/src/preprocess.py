def write_txt(data, path):
    with open(path, 'w') as f:
        for item in data:
            f.write(item + '\n')
    return data

def read_conll(path):
    src = []
    trg = []
    labels = []
    with open(path, 'r') as f:
        tmp_src = []
        tmp_label = []
        for line in f:
            line = line.replace('\n', '').split(' ')
            if line[0] == '':
                src.append(' '.join(tmp_src))
                trg.append(' '.join(tmp_label))
                tmp_src = []
                tmp_label = []
            else:
                tmp_src.append(line[0])
                try:
                    tmp_label.append(line[1])
                except:
                    tmp_label.append('O')
                if len(line) >= 2 and line[1] not in labels:
                    labels.append(line[1])
    print(labels)
    return src, trg


test_src, test_trg = read_conll('../data/vimq_word/test_word.conll')
dev_src, dev_trg = read_conll('../data/vimq_word/dev_word.conll')
tr_src, tr_trg = read_conll('../data/vimq_word/train_word.conll')

write_txt(test_src, '../data/vimq_word/test/seq.in')
write_txt(test_trg, '../data/vimq_word/test/seq.out')
write_txt(dev_src, '../data/vimq_word/dev/seq.in')
write_txt(dev_trg, '../data/vimq_word/dev/seq.out')
write_txt(tr_src, '../data/vimq_word/seq.in')
write_txt(tr_trg, '../data/vimq_word/train/seq.out')

a = ['O', 'B-drug', 'I-drug', 'B-medical_procedure', 'I-medical_procedure', 'B-SYMPTOM_AND_DISEASE', 'I-SYMPTOM_AND_DISEASE']
write_txt(a, 'data/vimq_word/slot_labels.txt')

