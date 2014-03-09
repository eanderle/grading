import argparse

parser = argparse.ArgumentParser()
parser.add_argument('total_score', type=int, help='total score of the test')
parser.add_argument('num_pages', type=int, help='number of pages in the test')

args = parser.parse_args()
while (True):
    final_score = float(args.total_score)
    for i in range(args.num_pages):
        final_score = final_score - float(raw_input('Points missed on page ' + str(i + 1) + ': '))
    print 'Final score: ' + str(final_score) + '\n'
