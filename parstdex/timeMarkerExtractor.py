import re
from parstdex.utils.pattern_to_regex import Patterns
from parstdex.utils.normalizer import Normalizer
from parstdex.utils.word_to_value import ValueExtractor


class MarkerExtractor:
    def __init__(self):
        # Normalizer: manage spaces, converts numbers to en, converts alphabet to fa
        self.normalizer = Normalizer()
        # Patterns: patterns to regex generator
        self.patterns = Patterns()
        # ValueExtractor: value extractor from known time and date
        self.extractor = ValueExtractor()

    def time_marker_extractor(self, input_sentence):
        """
        function should output list of strings, each item in list is a time marker present in the input sentence.
        :param input_sentence: input sentence
        :return:
        normalized_sentence: normalized sentence
        res: all extracted markers
        res_date: all extracted date values
        res_time: all extracted time values
        """

        # Normalizer: manage spaces, converts numbers to en, converts alphabet to fa
        normalizer = self.normalizer
        # Patterns: patterns to regex generator
        patterns = self.patterns
        # ValueExtractor: value extractor from known time and date
        extractor = self.extractor

        # apply normalizer on input sentence
        normalized_sentence = normalizer.normalize_cumulative(input_sentence)

        # define data structures to compute and postprocess the extracted patterns
        output_raw = {"Date": [], "Time": []}
        output_extracted = {}

        # add pattern keys to dictionaries and define a list structure for each key
        for key in patterns.regexes.keys():
            output_raw[key]: list = []
            output_extracted[key]: list = []

        # apply regexes on normalized sentence and store extracted markers in output_raw
        for key in patterns.regexes.keys():
            for regex_value in patterns.regexes[key]:
                # apply regex
                out = re.findall(fr'\b(?:{regex_value})', normalized_sentence)
                # ignore empty markers
                if len(out) > 0:
                    matches = list(re.finditer(fr'\b(?:{regex_value})', normalized_sentence))
                    # store extracted markers in output_raw
                    output_raw[key] = output_raw[key] + matches

        output_raw = output_raw
        spans = []
        for matches in output_raw.values():
            for match in matches:
                start = match.regs[0][0]
                end = match.regs[0][1]
                # match.group()
                spans.append((start, end))

        result = []
        pos = {
            'start': 0,
            'end': 1
        }
        # sort by start
        spans = sorted(spans, key=lambda x: (x[0], x[1]-x[0]))
        spans.append((spans[-1][pos['end']], spans[-1][pos['end']]))
        i = 0
        while i < len(spans)-1:
            # end(i) < start(i+1)
            if spans[i][pos['end']] < spans[i+1][pos['start']]:
                result.append(spans[i])
            # end(i)>=start(i+1)
            else:
                j = i
                max_end = spans[j][pos['end']]
                while max_end >= spans[j + 1][pos['start']]:
                    j += 1
                    if spans[j][pos['end']] > max_end:
                        max_end = spans[j][pos['end']]
                    if j == len(spans)-1:
                        break
                result.append((spans[i][pos['start']], max_end))
                i = j
            i += 1

        return normalized_sentence, result