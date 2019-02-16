# Loading the data files
import metrics
from files import get_filtered_data
from preprocessing import preprocess
from search import search_query
import csv
import string
import unicodedata


def read_testcases(path, system_paths):
    with open(path, newline='') as csvfile:
        r = csv.reader(csvfile)
        testcases = list(r)
        fname_indexes = filename_to_index(system_paths, list(zip(*testcases))[1])
        processed_testcases = []
        for i in range(len(testcases)):
            processed_testcases.append((testcases[i][0], fname_indexes[i]))
        return processed_testcases

def path_equal(system_path, testcase_path):
    # remove double filename such as .txt.txt
    system_path = system_path[:system_path.rfind('.')]

    # remove umlaut problem
    printable = set(string.printable)
    system_path = unicodedata.normalize('NFC', system_path)
    testcase_path = unicodedata.normalize('NFC', testcase_path)

    return system_path.endswith(testcase_path)

def filename_to_index(system_paths, testcase_paths):
    # match every testcase path
    indexes = []
    for t in testcase_paths:
        found = False
        for i, s in enumerate(system_paths):
            if path_equal(s, t):
                assert not found
                found = True
                indexes.append(i)
        assert found

    return indexes

def range_find(sorted_list, val):
    start, end = None, None
    for i in range(len(sorted_list)):
        if sorted_list[i] == val:
            if start is None:
                start = i
                end = i
            else:
                end += 1

    return start, end



def unit_test(rootDir, testcase_path, out_file):
    ''''''

    (file_data, file_dirs) = get_filtered_data(rootDir)
    tokens_filtered = preprocess(file_data)
    token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
    filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)
    print('Loading done.')

    testcases = read_testcases(testcase_path, file_dirs)

    testcase_pos = []
    testcase_pos_scored = []
    all_results = []

    for t in testcases:
        results = search_query(t[0], filentoken2tfidf, token2files, debug=True)
        all_results.append(results)
        # where is the testcase target?
        for i, r in enumerate(results):
            if r[1] == t[1]:
                # use the average of all positions with the the same score
                start, end = range_find(list(zip(*results))[0], r[0])
                testcase_pos_scored.append((end + start) / 2)
                testcase_pos.append(i)
                break
        else:
            # not found
            testcase_pos.append(-1)
            testcase_pos_scored.append(-1)

    # if not found, partial error 100
    error = sum(testcase_pos_scored)

    with open(out_file, 'w') as out:
        out.write('Total error: {} (sum of target pos)\nTestcase errors: {}\n'.format(error, ' '.join(map(str, testcase_pos_scored))))

        for i, t in enumerate(testcases):
            out.write('\n\n\n\nTESTCASE {}\nError: {}\nQuery: {}\n{}\n'.format(i + 1, testcase_pos_scored[i], t[0], '-'*50))
            for j, res in enumerate(all_results[i]):
                if testcase_pos[i] == j:
                    out.write('(target) ')
                out.write('score: {}, path: {}, explanation: {}\n'.format(*res))




if __name__ == '__main__':
    rootDir = 'docs_txt'
    testcase_file = 'test_queries.txt'
    eval_out = 'eval.txt'

    unit_test(rootDir, testcase_file, eval_out)
