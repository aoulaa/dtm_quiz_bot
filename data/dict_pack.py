# for users to get questions from DB

dict_of_topics = {
    '⬅️back': '⬅️back',
    'Test 2021 📑': 'test_2021',
    '1. VERB: Tense, Finite Forms Of The Verbs': 'verb',
    '2. VOICE(Passive and Active)': 'voice_active_passive',
    '3. MOOD': 'mood',
    '4. CONDITIONALS: Tenses in if and when Clauses. Tenses in Conditionals and Wishes.': 'Conditionals',
    '5. MODAL VERBS': 'modal_verbs',
    '6. NON-FINITE FORMS (verbs)': 'non_finite_verbs',
    '7. INDIRECT (reported) SPEECH': 'indirect_reported_speech',
    '8. PRONOUNS': 'pronouns',
    '9. ADJECTIVES AND ADVERBS': 'adjectives_adverbs',
    '10. ARTICLE': 'articles',
    '11. PREPOSITIONS': 'Prepositions',
    '12. CONJUNCTIONS': 'conjunctions',
    '13. QUESTIONS': 'questions',
    '14. SENTENCE STRUCTURE': 'sentence_structure',
    '15. MAKE UP A SENTENCE': 'make_sentence',
    '16. ERROR IDENTIFICATION': 'error_identification',
    '17. VOCABULARY: Antonyms': 'voc_antonyms',
    '18. VOCABULARY: Synonyms': 'voc_synonyms',
    '19. VOCABULARY: Word Usage': 'voc_word_usage',
    '20. LOGIC LIST': 'logic_list',
    '21. PERIPHRASIS': 'periphrasis',
    '22. SENTENCE LOGIC': 'sentence_logic',
    '23. ANSWER THE QUESTION': 'answer_question',
    '24. CHOOSE THE QUESTION': 'choose_question',
    '25. COMPLETE THE DIALOGUE': 'complete_dialog',

}

main_dict = dict_of_topics.copy()
main_dict.pop('⬅️back')


# for admins to check if the topic they want to add question does exist

list_of_topics = []
list_of_topics.extend(main_dict.values())

# for admins to choose from topics

topic_for_admins = ['bаck']
topic_for_admins.extend(main_dict.values())


# for admins


list_of_explain = ['Choose the correct answer.', ]


























# dict_of_topics = {
#     'Test 2019': 'test_2019',
#     'Test 2020': 'test_2020',
#     'Test 2021': 'test_2021',
#     'Nouns': 'noun',
#     'Compound nouns': 'compound_nouns',
#     'Forming the possessive form of nouns': 'form_possessive_nouns',
#     'Indefinite article a/an': 'indefinite_article',
#     'Definite article the': 'article_the',
#     'Articles with nouns in set expressions': 'article_nouns_set_expression',
#     'Articles with common nouns': 'articles_common_nouns',
#     'Articles with proper nouns': 'articles_proper_nouns',
#     'Personal/Objective Pronouns': 'personal_objective_pronouns',
#     'Possessive pronouns': 'possessive_pronouns',
#     'Reflexive pronoun': 'reflexive_pronoun',
#     'Demonstrative nouns': 'demonstrative_nouns',
#     'Indefinite pronouns, adverbials (some, any, no)': 'indefinite_pronoun_adverbials',
#     'Quantifier': 'quantifier',
#     'All/all of most/most of none etc': 'all_of_none_of',
#     'Distributives - both/neither/either etc': 'both_neither_etc',
#     'All every and whole': 'all_every_whole',
#     'Each, every, other, another': 'each_every_other_another',
#     'Adjectives & Adverbs sentence completion': 'adj_adver_sentence',
#     'adjectives ending -ing & -ed': 'adj_ending_ing_ed',
#     'Adjectives & Adverbs with exceptions well hard': 'adj_adver_execptions',
#     'So & such, enough & too the same, as': 'so_such_enough_too_etc',
#     'Comparison adjectives': 'comparison_adjectives',
#     'Superlative adjectives': 'superlative_adjectives',
#     'Comparison - much better/any better/ the sooner.. the better etc': 'comparison_much_better_etc',
#     'Comparison - as..as, not so..as. like, than': 'comparison_as_as_etc',
#     'Still/yet/already/any more etc': 'still_yet_already_etc',
#     'Viewpoint and commenting adverbs': 'viewpoint_commenting_adverbs',
#     'Adverbs of Certainty': 'adverbs_certainty',
#     'Verb + V-ing': 'verb_v_ing',
#     'Verb + to V': 'verb_to_verb',
#     'Complex object: Verb (+ object) + to V': 'complex_object_v',
#     'Verb + V-ing or to V': 'verb_ving_to_v',
#     'Preposition (in/for/about etc.) + V-ing': 'preposition_in_for_about_etc',
#     'To..,for..and so that': 'to_for_and_so_that',
#     'Adjective + to V': 'adjective_to_v',
#     'Can/could/be able to + V': 'can_could_be_able',
#     'Could(do)/could have (done)': 'could_do_could_have',
#     "Must/can't/have to/needn't": 'must_cant_have_to',
#     'May and Might': 'may_might',
#     'Should/would/had better': 'should_would_had_better',
#     'Requests/offers/permission/invitations': 'requests_offers_permission',
#     'Present simple': 'present_simple',
#     'Present Continuous': 'present_continuous',
#     'Present perfect/continuous': 'present_perfect_continuous',
#     'Past simple': 'past_simple',
#     'Past continuous': 'past_continuous',
#     'Past perfect': 'past_perfect',
#     'Past Perfect continuous': 'past_perfect_continuous',
#     'Future simple/to be going to': 'future_simple_to_be_going',
#     'Future continuous/perfect continuous': 'future_continuous_perfect_continuous',
#     'Construction: used to': 'construction_used_to',
#     'Passive Present': 'passive_present',
#     'Passive Past': 'passive_past',
#     'Passive Future': 'passive_future',
#     'Reported Statements': 'reported_statements',
#     'Reported Questions': 'reported_questions',
#     'Reported Orders/Requests': 'reported_orders',
#     'Tag Question': 'tag_question',
#     'I think so/I have so etc': 'think_so_have_so_etc',
#     'Relative clauses  who/that/which': 'relative_clause_who_that_which',
#     'Clauses with & without who/that/which': 'clauses_with_without_who_that',
#     'Clauses whose/whom/where': 'clauses_whose_whom_where',
#     'Clauses: extra information': 'clauses_extra_info',
#     'Clauses V-ing/V-ed(gerund, participle)': 'clauses_v_ing_v_ed',
#     'Although/though/even though/in split of/despite': 'although_though_even_though',
#     'Unless/As long as/provided/providing/in case': 'unless_as_long_as_provided',
#     'As/like and as/as if/as though': 'as_like_as_if_as_though',
#     'For/during and while': 'for_during_while',
#     'By/until': 'by_until',
#     'At/on/in/on in time/at the end & in the end(time)': 'at_on_in_on_in_time_at_the_end',
#     'In/at/on/by(position)': 'in_at_on_by_position',
#     'To/at/in/into(direction)': 'to_at_in_into_direction',
#     'In/on/at(other uses)': 'in_on_at_other',
#     'Noun + preposition': 'noun_preposition',
#     'Adjective + preposition': 'adjective_preposition',
#     'Verb + preposition': 'verb_preposition',
#     'Sentence completion': 'sentence_completion',
#     'Dialogue Completion': 'dialogue_completion',
#     'Text completion(missing part)': 'text_completion_missing',
#     'Text completion(right form of the verb)': 'text_completion_right',
#     'Gap filling(right form of the verb)': 'Gap filling_right',
#     'Gap filling(mixed:nouns, verb, Preposition etc)': 'gap_filling_mixed',
#     'Gap filling(choose the right part of speech)': 'gap_filling_choose_right_part',
#     'Numerals': 'numerals',
#     'Subjunctive mood/ unreal wishes(i wish)': 'subjunctive_mood_unreal_wishes',
#     'Conditional sentences': 'conditional_sentence',
#     'Give the right definition/synonym/antonym etc': 'give_right_definition_synonym'
# }


# bellow are data for topics
# list_nouns = ['🔙back', 'Nouns', 'Compound nouns',
#               'Forming the possessive form of nouns']
#
# list_articles = ['🔙back', 'Indefinite article a/an', 'Definite article the',
#                  'Articles with nouns in set expressions',
#                  'Articles with common nouns', 'Articles with proper nouns']
#
# list_pronouns = ['🔙back', 'Personal/Objective Pronouns', 'Possessive pronouns',
#                  'Reflexive pronoun', 'Demonstrative nouns',
#                  'Indefinite pronouns, adverbials (some, any, no)']
#
# list_quantifiers = ['🔙back', 'Quantifier', 'All/all of most/most of none etc',
#                     'Distributives - both/neither/either etc',
#                     'All every and whole', 'Each, every, other, another']
#
# list_Adjectives_adverbs = ['🔙back', 'Adjectives & Adverbs sentence completion', 'adjectives ending -ing & -ed',
#                            'Adjectives & Adverbs with exceptions well hard',
#                            'So & such, enough & too the same, as', 'Comparison adjectives',
#                            'Superlative adjectives', 'Comparison - much better/any better/ the sooner.. the better etc',
#                            'Comparison - as..as, not so..as. like, than', 'Still/yet/already/any more etc',
#                            'Viewpoint and commenting adverbs', 'Adverbs of Certainty'
#                            ]
#
# list_verb = ['🔙back', 'Verb + V-ing', 'Verb + to V', 'Complex object: Verb (+ object) + to V',
#              'Verb + V-ing or to V', 'Preposition (in/for/about etc.) + V-ing',
#              'To..,for..and so that', 'Adjective + to V']
#
# list_modal_verbs = ['🔙back', 'Can/could/be able to + V', 'Could(do)/could have (done)',
#                     "Must/can't/have to/needn't", 'May and Might', 'Should/would/had better',
#                     'Requests/offers/permission/invitations']
#
# list_tenses = ['🔙back', 'Present simple', 'Present Continuous', 'Present perfect/continuous',
#                'Past simple', 'Past continuous', 'Past perfect', 'Past Perfect continuous',
#                'Future simple/to be going to', 'Future continuous/perfect continuous',
#                'Construction: used to']
#
# list_passive = ['🔙back', 'Passive Present', 'Passive Past', 'Passive Future']
#
# list_reported_speech = ['🔙back', 'Reported Statements',
#                         'Reported Questions', 'Reported Orders/Requests']
#
# list_tag = ['🔙back', 'Tag Question', 'I think so/I have so etc']
#
# list_clauses = ['🔙back', 'Relative clauses  who/that/which', 'Clauses with & without who/that/which',
#                 'Clauses whose/whom/where', 'Clauses: extra information',
#                 'Clauses V-ing/V-ed(gerund, participle)']
#
# list_conjunction_preposition = ['🔙back', 'Although/though/even though/in split of/despite',
#                                 'Unless/As long as/provided/providing/in case',
#                                 'As/like and as/as if/as though', 'For/during and while',
#                                 'By/until', 'At/on/in/on in time/at the end & in the end(time)',
#                                 'In/at/on/by(position)', 'To/at/in/into(direction)', 'In/on/at(other uses)',
#                                 'Noun + preposition', 'Adjective + preposition', 'Verb + preposition',
#                                 ]
#
# list_completions = ['🔙back', 'Sentence completion', 'Dialogue Completion',
#                     'Text completion(missing part)', 'Text completion(right form of the verb)']
#
# list_gap_filling = ['🔙back', 'Gap filling(right form of the verb)', 'Gap filling(mixed:nouns, verb, Preposition etc)',
#                     'Gap filling(choose the right part of speech)']
#
# more = ['🔙back', 'Numerals',
#         'Subjunctive mood/ unreal wishes(i wish)',
#         'Conditional sentences',
#         'Give the right definition/synonym/antonym etc']
#
# years = ['🔙back', 'Test 2019', 'Test 2020', 'Test 2021']
# for buttons
# dict_nov_bar = {
#     'Tests by years': years,
#     'Nouns💡': list_nouns,
#     'Articles': list_articles,
#     'Pronouns': list_pronouns,
#     'Quantifiers': list_quantifiers,
#     'Adjectives and adverbs': list_Adjectives_adverbs,
#     'Verb': list_verb,
#     'Modal verbs': list_modal_verbs,
#     'Tenses': list_tenses,
#     'Passive voice': list_passive,
#     'Reported speech': list_reported_speech,
#     'Tag questions': list_tag,
#     'Clauses': list_clauses,
#     'Conjunction and Preposition': list_conjunction_preposition,
#     'Gap filling': list_gap_filling,
#     'More⬇️': more
#
# }
# dict for user interface
# main_topic = [
#     '⬅️back',
# ]
# main_topic.extend(dict_nov_bar.keys())

# lists for questions discription
