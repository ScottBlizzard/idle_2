# Control-Flip Diagnostic Results

## Main metrics

| model_id      | prompt_mode       |   pairs |   item_accuracy |   pair_accuracy |   pair_accuracy_ci_low |   pair_accuracy_ci_high |   flip_rate |   same_action_rate |   parse_rate |   final_parse_rate |
|:--------------|:------------------|--------:|----------------:|----------------:|-----------------------:|------------------------:|------------:|-------------------:|-------------:|-------------------:|
| qwen25_math7b | bellman           |     180 |           0.536 |           0.239 |                  0.178 |                   0.300 |       0.406 |              0.594 |        1.000 |              0.178 |
| qwen25_math7b | cot               |     180 |           0.625 |           0.300 |                  0.233 |                   0.367 |       0.350 |              0.644 |        0.997 |              0.028 |
| qwen25_math7b | direct            |     180 |           0.500 |           0.011 |                  0.000 |                   0.028 |       0.017 |              0.972 |        0.994 |              0.000 |
| qwen25_math7b | local_operator    |     180 |           0.586 |           0.239 |                  0.178 |                   0.300 |       0.306 |              0.694 |        1.000 |              0.003 |
| qwen25_math7b | positive_operator |     180 |           0.617 |           0.294 |                  0.228 |                   0.361 |       0.356 |              0.644 |        1.000 |              0.008 |
| qwen35_4b     | bellman           |     180 |           0.947 |           0.894 |                  0.850 |                   0.939 |       0.894 |              0.106 |        1.000 |              1.000 |
| qwen35_4b     | cot               |     180 |           0.953 |           0.906 |                  0.861 |                   0.944 |       0.906 |              0.094 |        1.000 |              1.000 |
| qwen35_4b     | direct            |     180 |           0.831 |           0.661 |                  0.594 |                   0.728 |       0.661 |              0.339 |        1.000 |              0.942 |
| qwen35_4b     | local_operator    |     180 |           0.947 |           0.894 |                  0.844 |                   0.939 |       0.894 |              0.106 |        1.000 |              1.000 |
| qwen35_4b     | positive_operator |     180 |           0.944 |           0.889 |                  0.839 |                   0.933 |       0.889 |              0.111 |        1.000 |              1.000 |
| qwen35_9b     | bellman           |     180 |           0.894 |           0.789 |                  0.728 |                   0.850 |       0.789 |              0.211 |        1.000 |              0.997 |
| qwen35_9b     | cot               |     180 |           0.986 |           0.972 |                  0.944 |                   0.994 |       0.972 |              0.028 |        1.000 |              0.950 |
| qwen35_9b     | direct            |     180 |           0.542 |           0.094 |                  0.056 |                   0.139 |       0.094 |              0.889 |        0.992 |              0.000 |
| qwen35_9b     | local_operator    |     180 |           0.914 |           0.828 |                  0.772 |                   0.878 |       0.828 |              0.172 |        1.000 |              0.183 |
| qwen35_9b     | positive_operator |     180 |           0.925 |           0.850 |                  0.794 |                   0.900 |       0.850 |              0.150 |        1.000 |              0.014 |
| qwen3_8b      | bellman           |     180 |           0.883 |           0.767 |                  0.706 |                   0.828 |       0.767 |              0.233 |        1.000 |              1.000 |
| qwen3_8b      | cot               |     180 |           0.806 |           0.639 |                  0.567 |                   0.706 |       0.650 |              0.294 |        0.969 |              0.244 |
| qwen3_8b      | direct            |     180 |           0.692 |           0.383 |                  0.311 |                   0.456 |       0.383 |              0.617 |        1.000 |              1.000 |
| qwen3_8b      | local_operator    |     180 |           0.889 |           0.778 |                  0.717 |                   0.839 |       0.778 |              0.222 |        1.000 |              0.692 |
| qwen3_8b      | positive_operator |     180 |           0.872 |           0.750 |                  0.683 |                   0.811 |       0.756 |              0.244 |        1.000 |              0.697 |

Pair accuracy is the primary metric: both members must be answered correctly. Random item choice yields 25% expected pair accuracy; always choosing the same root action yields 0% pair accuracy.

## Pre-registered decision

**NO-GO:** an ordinary compact chain-of-thought baseline reaches at least 90% pair accuracy.

## Error taxonomy

| model_id      | prompt_mode       | error_type     |   pairs |
|:--------------|:------------------|:---------------|--------:|
| qwen25_math7b | bellman           | branching_both |      85 |
| qwen25_math7b | bellman           | correct_flip   |      43 |
| qwen25_math7b | bellman           | reversed_flip  |      30 |
| qwen25_math7b | bellman           | safe_both      |      22 |
| qwen25_math7b | cot               | branching_both |     103 |
| qwen25_math7b | cot               | correct_flip   |      54 |
| qwen25_math7b | cot               | safe_both      |      13 |
| qwen25_math7b | cot               | reversed_flip  |       9 |
| qwen25_math7b | cot               | unparsed       |       1 |
| qwen25_math7b | direct            | safe_both      |     175 |
| qwen25_math7b | direct            | correct_flip   |       2 |
| qwen25_math7b | direct            | unparsed       |       2 |
| qwen25_math7b | direct            | reversed_flip  |       1 |
| qwen25_math7b | local_operator    | branching_both |     113 |
| qwen25_math7b | local_operator    | correct_flip   |      43 |
| qwen25_math7b | local_operator    | reversed_flip  |      12 |
| qwen25_math7b | local_operator    | safe_both      |      12 |
| qwen25_math7b | positive_operator | branching_both |     107 |
| qwen25_math7b | positive_operator | correct_flip   |      53 |
| qwen25_math7b | positive_operator | reversed_flip  |      11 |
| qwen25_math7b | positive_operator | safe_both      |       9 |
| qwen35_4b     | bellman           | correct_flip   |     161 |
| qwen35_4b     | bellman           | branching_both |      18 |
| qwen35_4b     | bellman           | safe_both      |       1 |
| qwen35_4b     | cot               | correct_flip   |     163 |
| qwen35_4b     | cot               | branching_both |      16 |
| qwen35_4b     | cot               | safe_both      |       1 |
| qwen35_4b     | direct            | correct_flip   |     119 |
| qwen35_4b     | direct            | safe_both      |      36 |
| qwen35_4b     | direct            | branching_both |      25 |
| qwen35_4b     | local_operator    | correct_flip   |     161 |
| qwen35_4b     | local_operator    | branching_both |      18 |
| qwen35_4b     | local_operator    | safe_both      |       1 |
| qwen35_4b     | positive_operator | correct_flip   |     160 |
| qwen35_4b     | positive_operator | branching_both |      18 |
| qwen35_4b     | positive_operator | safe_both      |       2 |
| qwen35_9b     | bellman           | correct_flip   |     142 |
| qwen35_9b     | bellman           | branching_both |      36 |
| qwen35_9b     | bellman           | safe_both      |       2 |
| qwen35_9b     | cot               | correct_flip   |     175 |
| qwen35_9b     | cot               | branching_both |       4 |
| qwen35_9b     | cot               | safe_both      |       1 |
| qwen35_9b     | direct            | safe_both      |     160 |
| qwen35_9b     | direct            | correct_flip   |      17 |
| qwen35_9b     | direct            | unparsed       |       3 |
| qwen35_9b     | local_operator    | correct_flip   |     149 |
| qwen35_9b     | local_operator    | branching_both |      30 |
| qwen35_9b     | local_operator    | safe_both      |       1 |
| qwen35_9b     | positive_operator | correct_flip   |     153 |
| qwen35_9b     | positive_operator | branching_both |      25 |
| qwen35_9b     | positive_operator | safe_both      |       2 |
| qwen3_8b      | bellman           | correct_flip   |     138 |
| qwen3_8b      | bellman           | branching_both |      36 |
| qwen3_8b      | bellman           | safe_both      |       6 |
| qwen3_8b      | cot               | correct_flip   |     115 |
| qwen3_8b      | cot               | branching_both |      48 |
| qwen3_8b      | cot               | unparsed       |      10 |
| qwen3_8b      | cot               | safe_both      |       5 |
| qwen3_8b      | cot               | reversed_flip  |       2 |
| qwen3_8b      | direct            | branching_both |     108 |
| qwen3_8b      | direct            | correct_flip   |      69 |
| qwen3_8b      | direct            | safe_both      |       3 |
| qwen3_8b      | local_operator    | correct_flip   |     140 |
| qwen3_8b      | local_operator    | branching_both |      36 |
| qwen3_8b      | local_operator    | safe_both      |       4 |
| qwen3_8b      | positive_operator | correct_flip   |     135 |
| qwen3_8b      | positive_operator | branching_both |      34 |
| qwen3_8b      | positive_operator | safe_both      |      10 |
| qwen3_8b      | positive_operator | reversed_flip  |       1 |

## Prompt gains

| model_id      | prompt_mode       |   direct_pair_accuracy |   scaffold_pair_accuracy |   absolute_gain |   remaining_gap_closed |
|:--------------|:------------------|-----------------------:|-------------------------:|----------------:|-----------------------:|
| qwen25_math7b | cot               |                  0.011 |                    0.300 |           0.289 |                  0.292 |
| qwen25_math7b | bellman           |                  0.011 |                    0.239 |           0.228 |                  0.230 |
| qwen25_math7b | local_operator    |                  0.011 |                    0.239 |           0.228 |                  0.230 |
| qwen25_math7b | positive_operator |                  0.011 |                    0.294 |           0.283 |                  0.287 |
| qwen35_4b     | cot               |                  0.661 |                    0.906 |           0.244 |                  0.721 |
| qwen35_4b     | bellman           |                  0.661 |                    0.894 |           0.233 |                  0.689 |
| qwen35_4b     | local_operator    |                  0.661 |                    0.894 |           0.233 |                  0.689 |
| qwen35_4b     | positive_operator |                  0.661 |                    0.889 |           0.228 |                  0.672 |
| qwen35_9b     | cot               |                  0.094 |                    0.972 |           0.878 |                  0.969 |
| qwen35_9b     | bellman           |                  0.094 |                    0.789 |           0.694 |                  0.767 |
| qwen35_9b     | local_operator    |                  0.094 |                    0.828 |           0.733 |                  0.810 |
| qwen35_9b     | positive_operator |                  0.094 |                    0.850 |           0.756 |                  0.834 |
| qwen3_8b      | cot               |                  0.383 |                    0.639 |           0.256 |                  0.414 |
| qwen3_8b      | bellman           |                  0.383 |                    0.767 |           0.383 |                  0.622 |
| qwen3_8b      | local_operator    |                  0.383 |                    0.778 |           0.394 |                  0.640 |
| qwen3_8b      | positive_operator |                  0.383 |                    0.750 |           0.367 |                  0.595 |

Paired prompt differences are available in `prompt_comparisons.csv`.

## Difficulty breakdown

| model_id      | prompt_mode       |   difficulty |   pairs |   pair_accuracy |   self_accuracy |   opponent_accuracy |   flip_rate |   same_action_rate |
|:--------------|:------------------|-------------:|--------:|----------------:|----------------:|--------------------:|------------:|-------------------:|
| qwen25_math7b | bellman           |            1 |      60 |           0.400 |           0.783 |               0.500 |       0.517 |              0.483 |
| qwen25_math7b | bellman           |            2 |      60 |           0.167 |           0.617 |               0.367 |       0.350 |              0.650 |
| qwen25_math7b | bellman           |            3 |      60 |           0.150 |           0.733 |               0.217 |       0.350 |              0.650 |
| qwen25_math7b | cot               |            1 |      60 |           0.500 |           0.817 |               0.650 |       0.533 |              0.467 |
| qwen25_math7b | cot               |            2 |      60 |           0.250 |           0.833 |               0.300 |       0.367 |              0.633 |
| qwen25_math7b | cot               |            3 |      60 |           0.150 |           0.983 |               0.167 |       0.150 |              0.833 |
| qwen25_math7b | direct            |            1 |      60 |           0.000 |           0.000 |               0.983 |       0.000 |              0.967 |
| qwen25_math7b | direct            |            2 |      60 |           0.000 |           0.000 |               0.983 |       0.017 |              0.983 |
| qwen25_math7b | direct            |            3 |      60 |           0.033 |           0.033 |               1.000 |       0.033 |              0.967 |
| qwen25_math7b | local_operator    |            1 |      60 |           0.383 |           0.850 |               0.500 |       0.417 |              0.583 |
| qwen25_math7b | local_operator    |            2 |      60 |           0.167 |           0.833 |               0.250 |       0.250 |              0.750 |
| qwen25_math7b | local_operator    |            3 |      60 |           0.167 |           0.917 |               0.167 |       0.250 |              0.750 |
| qwen25_math7b | positive_operator |            1 |      60 |           0.450 |           0.950 |               0.483 |       0.467 |              0.533 |
| qwen25_math7b | positive_operator |            2 |      60 |           0.283 |           0.767 |               0.383 |       0.417 |              0.583 |
| qwen25_math7b | positive_operator |            3 |      60 |           0.150 |           0.950 |               0.167 |       0.183 |              0.817 |
| qwen35_4b     | bellman           |            1 |      60 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | bellman           |            2 |      60 |           0.883 |           1.000 |               0.883 |       0.883 |              0.117 |
| qwen35_4b     | bellman           |            3 |      60 |           0.833 |           0.983 |               0.850 |       0.833 |              0.167 |
| qwen35_4b     | cot               |            1 |      60 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | cot               |            2 |      60 |           0.933 |           1.000 |               0.933 |       0.933 |              0.067 |
| qwen35_4b     | cot               |            3 |      60 |           0.883 |           0.983 |               0.900 |       0.883 |              0.117 |
| qwen35_4b     | direct            |            1 |      60 |           0.800 |           0.983 |               0.817 |       0.800 |              0.200 |
| qwen35_4b     | direct            |            2 |      60 |           0.600 |           0.767 |               0.833 |       0.600 |              0.400 |
| qwen35_4b     | direct            |            3 |      60 |           0.583 |           0.650 |               0.933 |       0.583 |              0.417 |
| qwen35_4b     | local_operator    |            1 |      60 |           0.917 |           1.000 |               0.917 |       0.917 |              0.083 |
| qwen35_4b     | local_operator    |            2 |      60 |           0.883 |           1.000 |               0.883 |       0.883 |              0.117 |
| qwen35_4b     | local_operator    |            3 |      60 |           0.883 |           0.983 |               0.900 |       0.883 |              0.117 |
| qwen35_4b     | positive_operator |            1 |      60 |           0.850 |           1.000 |               0.850 |       0.850 |              0.150 |
| qwen35_4b     | positive_operator |            2 |      60 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | positive_operator |            3 |      60 |           0.850 |           0.967 |               0.883 |       0.850 |              0.150 |
| qwen35_9b     | bellman           |            1 |      60 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_9b     | bellman           |            2 |      60 |           0.733 |           0.983 |               0.750 |       0.733 |              0.267 |
| qwen35_9b     | bellman           |            3 |      60 |           0.767 |           0.983 |               0.783 |       0.767 |              0.233 |
| qwen35_9b     | cot               |            1 |      60 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_9b     | cot               |            2 |      60 |           0.983 |           1.000 |               0.983 |       0.983 |              0.017 |
| qwen35_9b     | cot               |            3 |      60 |           0.967 |           0.983 |               0.983 |       0.967 |              0.033 |
| qwen35_9b     | direct            |            1 |      60 |           0.083 |           0.083 |               0.983 |       0.083 |              0.900 |
| qwen35_9b     | direct            |            2 |      60 |           0.100 |           0.100 |               0.983 |       0.100 |              0.883 |
| qwen35_9b     | direct            |            3 |      60 |           0.100 |           0.100 |               1.000 |       0.100 |              0.883 |
| qwen35_9b     | local_operator    |            1 |      60 |           0.750 |           1.000 |               0.750 |       0.750 |              0.250 |
| qwen35_9b     | local_operator    |            2 |      60 |           0.833 |           1.000 |               0.833 |       0.833 |              0.167 |
| qwen35_9b     | local_operator    |            3 |      60 |           0.900 |           0.983 |               0.917 |       0.900 |              0.100 |
| qwen35_9b     | positive_operator |            1 |      60 |           0.750 |           1.000 |               0.750 |       0.750 |              0.250 |
| qwen35_9b     | positive_operator |            2 |      60 |           0.883 |           1.000 |               0.883 |       0.883 |              0.117 |
| qwen35_9b     | positive_operator |            3 |      60 |           0.917 |           0.967 |               0.950 |       0.917 |              0.083 |
| qwen3_8b      | bellman           |            1 |      60 |           0.717 |           0.900 |               0.817 |       0.717 |              0.283 |
| qwen3_8b      | bellman           |            2 |      60 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen3_8b      | bellman           |            3 |      60 |           0.783 |           1.000 |               0.783 |       0.783 |              0.217 |
| qwen3_8b      | cot               |            1 |      60 |           0.683 |           0.917 |               0.733 |       0.683 |              0.250 |
| qwen3_8b      | cot               |            2 |      60 |           0.617 |           0.933 |               0.667 |       0.617 |              0.300 |
| qwen3_8b      | cot               |            3 |      60 |           0.617 |           0.900 |               0.683 |       0.650 |              0.333 |
| qwen3_8b      | direct            |            1 |      60 |           0.617 |           0.950 |               0.667 |       0.617 |              0.383 |
| qwen3_8b      | direct            |            2 |      60 |           0.283 |           1.000 |               0.283 |       0.283 |              0.717 |
| qwen3_8b      | direct            |            3 |      60 |           0.250 |           1.000 |               0.250 |       0.250 |              0.750 |
| qwen3_8b      | local_operator    |            1 |      60 |           0.783 |           1.000 |               0.783 |       0.783 |              0.217 |
| qwen3_8b      | local_operator    |            2 |      60 |           0.767 |           0.967 |               0.800 |       0.767 |              0.233 |
| qwen3_8b      | local_operator    |            3 |      60 |           0.783 |           0.967 |               0.817 |       0.783 |              0.217 |
| qwen3_8b      | positive_operator |            1 |      60 |           0.750 |           1.000 |               0.750 |       0.750 |              0.250 |
| qwen3_8b      | positive_operator |            2 |      60 |           0.750 |           0.883 |               0.850 |       0.767 |              0.233 |
| qwen3_8b      | positive_operator |            3 |      60 |           0.750 |           0.933 |               0.817 |       0.750 |              0.250 |

## Domain breakdown

| model_id      | prompt_mode       | domain        |   pairs |   pair_accuracy |   self_accuracy |   opponent_accuracy |   flip_rate |   same_action_rate |
|:--------------|:------------------|:--------------|--------:|----------------:|----------------:|--------------------:|------------:|-------------------:|
| qwen25_math7b | bellman           | abstract_game |      30 |           0.133 |           0.833 |               0.200 |       0.233 |              0.767 |
| qwen25_math7b | bellman           | cyber_defense |      30 |           0.367 |           0.633 |               0.533 |       0.567 |              0.433 |
| qwen25_math7b | bellman           | exploration   |      30 |           0.333 |           0.733 |               0.467 |       0.467 |              0.533 |
| qwen25_math7b | bellman           | logistics     |      30 |           0.167 |           0.700 |               0.333 |       0.300 |              0.700 |
| qwen25_math7b | bellman           | resource_game |      30 |           0.233 |           0.600 |               0.333 |       0.533 |              0.467 |
| qwen25_math7b | bellman           | tool_agent    |      30 |           0.200 |           0.767 |               0.300 |       0.333 |              0.667 |
| qwen25_math7b | cot               | abstract_game |      30 |           0.367 |           0.800 |               0.500 |       0.433 |              0.567 |
| qwen25_math7b | cot               | cyber_defense |      30 |           0.267 |           0.900 |               0.333 |       0.300 |              0.700 |
| qwen25_math7b | cot               | exploration   |      30 |           0.333 |           0.867 |               0.400 |       0.400 |              0.600 |
| qwen25_math7b | cot               | logistics     |      30 |           0.267 |           0.867 |               0.333 |       0.333 |              0.667 |
| qwen25_math7b | cot               | resource_game |      30 |           0.300 |           0.900 |               0.367 |       0.333 |              0.667 |
| qwen25_math7b | cot               | tool_agent    |      30 |           0.267 |           0.933 |               0.300 |       0.300 |              0.667 |
| qwen25_math7b | direct            | abstract_game |      30 |           0.067 |           0.067 |               0.967 |       0.067 |              0.867 |
| qwen25_math7b | direct            | cyber_defense |      30 |           0.000 |           0.000 |               1.000 |       0.000 |              1.000 |
| qwen25_math7b | direct            | exploration   |      30 |           0.000 |           0.000 |               1.000 |       0.000 |              1.000 |
| qwen25_math7b | direct            | logistics     |      30 |           0.000 |           0.000 |               0.967 |       0.033 |              0.967 |
| qwen25_math7b | direct            | resource_game |      30 |           0.000 |           0.000 |               1.000 |       0.000 |              1.000 |
| qwen25_math7b | direct            | tool_agent    |      30 |           0.000 |           0.000 |               1.000 |       0.000 |              1.000 |
| qwen25_math7b | local_operator    | abstract_game |      30 |           0.333 |           0.767 |               0.500 |       0.400 |              0.600 |
| qwen25_math7b | local_operator    | cyber_defense |      30 |           0.200 |           0.867 |               0.267 |       0.267 |              0.733 |
| qwen25_math7b | local_operator    | exploration   |      30 |           0.167 |           0.933 |               0.200 |       0.200 |              0.800 |
| qwen25_math7b | local_operator    | logistics     |      30 |           0.233 |           0.867 |               0.267 |       0.333 |              0.667 |
| qwen25_math7b | local_operator    | resource_game |      30 |           0.300 |           0.933 |               0.367 |       0.300 |              0.700 |
| qwen25_math7b | local_operator    | tool_agent    |      30 |           0.200 |           0.833 |               0.233 |       0.333 |              0.667 |
| qwen25_math7b | positive_operator | abstract_game |      30 |           0.267 |           0.800 |               0.400 |       0.333 |              0.667 |
| qwen25_math7b | positive_operator | cyber_defense |      30 |           0.133 |           0.900 |               0.133 |       0.233 |              0.767 |
| qwen25_math7b | positive_operator | exploration   |      30 |           0.233 |           0.833 |               0.333 |       0.300 |              0.700 |
| qwen25_math7b | positive_operator | logistics     |      30 |           0.400 |           0.933 |               0.433 |       0.433 |              0.567 |
| qwen25_math7b | positive_operator | resource_game |      30 |           0.233 |           0.933 |               0.267 |       0.267 |              0.733 |
| qwen25_math7b | positive_operator | tool_agent    |      30 |           0.500 |           0.933 |               0.500 |       0.567 |              0.433 |
| qwen35_4b     | bellman           | abstract_game |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | bellman           | cyber_defense |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_4b     | bellman           | exploration   |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_4b     | bellman           | logistics     |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | bellman           | resource_game |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | bellman           | tool_agent    |      30 |           0.933 |           0.967 |               0.967 |       0.933 |              0.067 |
| qwen35_4b     | cot               | abstract_game |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | cot               | cyber_defense |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_4b     | cot               | exploration   |      30 |           0.900 |           0.967 |               0.933 |       0.900 |              0.100 |
| qwen35_4b     | cot               | logistics     |      30 |           0.733 |           1.000 |               0.733 |       0.733 |              0.267 |
| qwen35_4b     | cot               | resource_game |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | cot               | tool_agent    |      30 |           1.000 |           1.000 |               1.000 |       1.000 |              0.000 |
| qwen35_4b     | direct            | abstract_game |      30 |           0.733 |           0.867 |               0.867 |       0.733 |              0.267 |
| qwen35_4b     | direct            | cyber_defense |      30 |           0.400 |           0.833 |               0.567 |       0.400 |              0.600 |
| qwen35_4b     | direct            | exploration   |      30 |           0.667 |           0.767 |               0.900 |       0.667 |              0.333 |
| qwen35_4b     | direct            | logistics     |      30 |           0.600 |           0.667 |               0.933 |       0.600 |              0.400 |
| qwen35_4b     | direct            | resource_game |      30 |           0.667 |           0.767 |               0.900 |       0.667 |              0.333 |
| qwen35_4b     | direct            | tool_agent    |      30 |           0.900 |           0.900 |               1.000 |       0.900 |              0.100 |
| qwen35_4b     | local_operator    | abstract_game |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | local_operator    | cyber_defense |      30 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen35_4b     | local_operator    | exploration   |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | local_operator    | logistics     |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_4b     | local_operator    | resource_game |      30 |           0.900 |           0.967 |               0.933 |       0.900 |              0.100 |
| qwen35_4b     | local_operator    | tool_agent    |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | positive_operator | abstract_game |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_4b     | positive_operator | cyber_defense |      30 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen35_4b     | positive_operator | exploration   |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_4b     | positive_operator | logistics     |      30 |           0.867 |           0.967 |               0.900 |       0.867 |              0.133 |
| qwen35_4b     | positive_operator | resource_game |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_4b     | positive_operator | tool_agent    |      30 |           0.967 |           0.967 |               1.000 |       0.967 |              0.033 |
| qwen35_9b     | bellman           | abstract_game |      30 |           0.900 |           0.967 |               0.933 |       0.900 |              0.100 |
| qwen35_9b     | bellman           | cyber_defense |      30 |           0.733 |           1.000 |               0.733 |       0.733 |              0.267 |
| qwen35_9b     | bellman           | exploration   |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_9b     | bellman           | logistics     |      30 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen35_9b     | bellman           | resource_game |      30 |           0.667 |           1.000 |               0.667 |       0.667 |              0.333 |
| qwen35_9b     | bellman           | tool_agent    |      30 |           0.733 |           0.967 |               0.767 |       0.733 |              0.267 |
| qwen35_9b     | cot               | abstract_game |      30 |           1.000 |           1.000 |               1.000 |       1.000 |              0.000 |
| qwen35_9b     | cot               | cyber_defense |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen35_9b     | cot               | exploration   |      30 |           0.933 |           1.000 |               0.933 |       0.933 |              0.067 |
| qwen35_9b     | cot               | logistics     |      30 |           1.000 |           1.000 |               1.000 |       1.000 |              0.000 |
| qwen35_9b     | cot               | resource_game |      30 |           0.933 |           0.967 |               0.967 |       0.933 |              0.067 |
| qwen35_9b     | cot               | tool_agent    |      30 |           1.000 |           1.000 |               1.000 |       1.000 |              0.000 |
| qwen35_9b     | direct            | abstract_game |      30 |           0.100 |           0.100 |               1.000 |       0.100 |              0.900 |
| qwen35_9b     | direct            | cyber_defense |      30 |           0.000 |           0.000 |               0.933 |       0.000 |              0.933 |
| qwen35_9b     | direct            | exploration   |      30 |           0.100 |           0.100 |               1.000 |       0.100 |              0.900 |
| qwen35_9b     | direct            | logistics     |      30 |           0.133 |           0.133 |               1.000 |       0.133 |              0.867 |
| qwen35_9b     | direct            | resource_game |      30 |           0.100 |           0.100 |               1.000 |       0.100 |              0.867 |
| qwen35_9b     | direct            | tool_agent    |      30 |           0.133 |           0.133 |               1.000 |       0.133 |              0.867 |
| qwen35_9b     | local_operator    | abstract_game |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_9b     | local_operator    | cyber_defense |      30 |           0.700 |           1.000 |               0.700 |       0.700 |              0.300 |
| qwen35_9b     | local_operator    | exploration   |      30 |           0.733 |           0.967 |               0.767 |       0.733 |              0.267 |
| qwen35_9b     | local_operator    | logistics     |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_9b     | local_operator    | resource_game |      30 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen35_9b     | local_operator    | tool_agent    |      30 |           0.933 |           1.000 |               0.933 |       0.933 |              0.067 |
| qwen35_9b     | positive_operator | abstract_game |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen35_9b     | positive_operator | cyber_defense |      30 |           0.667 |           1.000 |               0.667 |       0.667 |              0.333 |
| qwen35_9b     | positive_operator | exploration   |      30 |           0.800 |           0.967 |               0.833 |       0.800 |              0.200 |
| qwen35_9b     | positive_operator | logistics     |      30 |           0.900 |           0.967 |               0.933 |       0.900 |              0.100 |
| qwen35_9b     | positive_operator | resource_game |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen35_9b     | positive_operator | tool_agent    |      30 |           0.967 |           1.000 |               0.967 |       0.967 |              0.033 |
| qwen3_8b      | bellman           | abstract_game |      30 |           0.700 |           0.867 |               0.833 |       0.700 |              0.300 |
| qwen3_8b      | bellman           | cyber_defense |      30 |           0.700 |           1.000 |               0.700 |       0.700 |              0.300 |
| qwen3_8b      | bellman           | exploration   |      30 |           0.733 |           0.967 |               0.767 |       0.733 |              0.267 |
| qwen3_8b      | bellman           | logistics     |      30 |           0.833 |           1.000 |               0.833 |       0.833 |              0.167 |
| qwen3_8b      | bellman           | resource_game |      30 |           0.733 |           0.967 |               0.767 |       0.733 |              0.267 |
| qwen3_8b      | bellman           | tool_agent    |      30 |           0.900 |           1.000 |               0.900 |       0.900 |              0.100 |
| qwen3_8b      | cot               | abstract_game |      30 |           0.767 |           1.000 |               0.767 |       0.767 |              0.233 |
| qwen3_8b      | cot               | cyber_defense |      30 |           0.433 |           0.800 |               0.600 |       0.433 |              0.467 |
| qwen3_8b      | cot               | exploration   |      30 |           0.533 |           0.833 |               0.600 |       0.600 |              0.267 |
| qwen3_8b      | cot               | logistics     |      30 |           0.667 |           0.967 |               0.700 |       0.667 |              0.333 |
| qwen3_8b      | cot               | resource_game |      30 |           0.567 |           0.967 |               0.600 |       0.567 |              0.400 |
| qwen3_8b      | cot               | tool_agent    |      30 |           0.867 |           0.933 |               0.900 |       0.867 |              0.067 |
| qwen3_8b      | direct            | abstract_game |      30 |           0.567 |           0.933 |               0.633 |       0.567 |              0.433 |
| qwen3_8b      | direct            | cyber_defense |      30 |           0.200 |           0.967 |               0.233 |       0.200 |              0.800 |
| qwen3_8b      | direct            | exploration   |      30 |           0.233 |           1.000 |               0.233 |       0.233 |              0.767 |
| qwen3_8b      | direct            | logistics     |      30 |           0.367 |           1.000 |               0.367 |       0.367 |              0.633 |
| qwen3_8b      | direct            | resource_game |      30 |           0.467 |           1.000 |               0.467 |       0.467 |              0.533 |
| qwen3_8b      | direct            | tool_agent    |      30 |           0.467 |           1.000 |               0.467 |       0.467 |              0.533 |
| qwen3_8b      | local_operator    | abstract_game |      30 |           0.767 |           1.000 |               0.767 |       0.767 |              0.233 |
| qwen3_8b      | local_operator    | cyber_defense |      30 |           0.567 |           0.867 |               0.700 |       0.567 |              0.433 |
| qwen3_8b      | local_operator    | exploration   |      30 |           0.733 |           1.000 |               0.733 |       0.733 |              0.267 |
| qwen3_8b      | local_operator    | logistics     |      30 |           0.867 |           1.000 |               0.867 |       0.867 |              0.133 |
| qwen3_8b      | local_operator    | resource_game |      30 |           0.800 |           1.000 |               0.800 |       0.800 |              0.200 |
| qwen3_8b      | local_operator    | tool_agent    |      30 |           0.933 |           1.000 |               0.933 |       0.933 |              0.067 |
| qwen3_8b      | positive_operator | abstract_game |      30 |           0.733 |           0.967 |               0.767 |       0.733 |              0.267 |
| qwen3_8b      | positive_operator | cyber_defense |      30 |           0.533 |           0.867 |               0.633 |       0.567 |              0.433 |
| qwen3_8b      | positive_operator | exploration   |      30 |           0.700 |           0.967 |               0.733 |       0.700 |              0.300 |
| qwen3_8b      | positive_operator | logistics     |      30 |           0.833 |           0.900 |               0.933 |       0.833 |              0.167 |
| qwen3_8b      | positive_operator | resource_game |      30 |           0.867 |           0.967 |               0.900 |       0.867 |              0.133 |
| qwen3_8b      | positive_operator | tool_agent    |      30 |           0.833 |           0.967 |               0.867 |       0.833 |              0.167 |

## Interpretation guardrails

- High item accuracy with low pair accuracy indicates controller-insensitive answers, not arithmetic inability alone.
- A large `safe_both` count indicates global uncertainty aversion; `branching_both` indicates global option/variance seeking.
- If Bellman scaffolding removes the effect, the result does not support a fundamental planning limitation.
- Synthetic success is only a diagnostic. It cannot by itself support an ICLR main-track claim.
