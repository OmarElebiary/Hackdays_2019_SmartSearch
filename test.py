# Loading the data files
import metrics
from files import get_filtered_data
from preprocessing import preprocess
from search import search_query
import csv


def read_testcases(path):
    with open(path, newline='') as csvfile:
        r = csv.reader(csvfile)
        return list(r)


def path_equal(system_path, testcase_path):
    # remove double filename such as .txt.txt
    system_path = system_path[:system_path.rfind('.')]

    return system_path.endswith(testcase_path)


def unit_test(rootDir, testcase_path, out_file):
    ''''''
    testcases = read_testcases(testcase_path)

    (file_data, file_dirs) = get_filtered_data(rootDir)
    tokens_filtered = preprocess(file_data)
    token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
    filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)
    print('Loading done.')

    testcase_pos = []
    all_results = []

    for t in testcases:
        results = search_query(t[0], filentoken2tfidf, token2files, debug=True)
        all_results.append(results)
        # where is the testcase target?
        for i, r in enumerate(results):
            if path_equal(file_dirs[r[1]], t[1]):
                testcase_pos.append(i)
                break
        else:
            # not found
            testcase_pos.append(-1)

    # if not found, partial error 100
    testcase_errors = list(map(lambda x: 100 if x == -1 else x, testcase_pos))
    error = sum(testcase_errors)

    with open(out_file, 'w') as out:
        out.write('Total error: {} (sum of target pos)\nTestcase errors: {}\n'.format(error, ' '.join(map(str, testcase_errors))))

        for i, t in enumerate(testcases):
            out.write('\n\n\n\nTESTCASE {}\nError: {}\nQuery: {}\n{}\n'.format(i + 1, testcase_errors[i], t[0], '-'*50))
            for j, res in enumerate(all_results[i]):
                if testcase_pos[i] == j:
                    out.write('(target) ')
                out.write('score: {}, path: {}, explanation: {}\n'.format(*res))




if __name__ == '__main__':
    rootDir = '../docs_txt'
    testcase_file = 'test_queries.txt'
    eval_out = 'eval.txt'

    unit_test(rootDir, testcase_file, eval_out)
