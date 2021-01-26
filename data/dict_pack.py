# for users to get questions from DB
dict_of_topics = {
    'Present simple': 'present_simple',
    'Past simple': 'past_simple',
    'Nouns': 'noun',
    'Compound nouns': 'compound_nouns',
    'Forming the possessive form of nouns': 'form_possessive_nouns',
    'Indefinite article a/an': 'indefinite_article',
    'Definite article the': 'article_the',
    'Articles with nouns in set expressions': 'article_nouns_set_expression',
    'Articles with common nouns': 'articles_common_nouns',
    'Articles with proper nouns': 'articles_proper_nouns',
    'Personal/Objective Pronouns': 'personal_objective_pronouns',
    'Possessive pronouns': 'possessive_pronouns',
    'Reflexive pronoun': 'reflexive_pronoun',
    'Demonstrative nouns': 'demonstrative_nouns',
    'Indefinite pronouns, adverbials (some, any, no)': 'indefinite_pronoun_adverbials',
    'Quantifier': 'quantifier',
    'All/all of most/most of none etc': 'all_of_none_of',
    'Distributives - both/neither/either etc': 'both_neither_etc',
    'All every and whole': 'all_every_whole',
    'Each, every, other, another': 'each_every_other_another',
    'Adjectives & Adverbs sentence completion': 'adj_adver_sentence',
    'adjectives ending -ing & -ed': 'adj_ending_ing_ed',
    'Adjectives & Adverbs with exceptions well hard': 'adj_adver_execptions',
    'So & such, enough & too the same, as': 'so_such_enough_too_etc',
    'Comparison adjectives': 'comparison_adjectives',
    'Superlative adjectives': 'superlative_adjectives',
    'Comparison - much better/any better/ the sooner.. the better etc': 'comparison_much_better_etc',
    'Comparison - as..as, not so..as. like, than': 'comparison_as_as_etc',
    'Still/yet/already/any more etc': 'still_yet_already_etc',
    'Viewpoint and commenting adverbs': 'viewpoint_commenting_adverbs',
    'Adverbs of Certainty': 'adverbs_certainty',




}

# for admins to check if the topic they want to add question does exist
list_of_topics = []
list_of_topics.extend(dict_of_topics.values())

# for admins to choose from topics
topic_for_admins = ['bаck']
topic_for_admins.extend(dict_of_topics.values())


# bellow are data for topics
list_nouns = ['🔙back', 'Nouns', 'Compound nouns',
              'Forming the possessive form of nouns']

list_articles = ['🔙back', 'Indefinite article a/an', 'Definite article the',
                 'Articles with nouns in set expressions',
                 'Articles with common nouns', 'Articles with proper nouns']


list_pronouns = ['🔙back', 'Personal/Objective Pronouns', 'Possessive pronouns',
                 'Reflexive pronoun', 'Demonstrative nouns',
                 'Indefinite pronouns, adverbials (some, any, no)']

list_quantifiers = ['🔙back', 'Quantifier', 'All/all of most/most of none etc',
                    'Distributives - both/neither/either etc',
                    'All every and whole', 'Each, every, other, another']

list_Adjectives_adverbs = ['🔙back', 'Adjectives & Adverbs sentence completion', 'adjectives ending -ing & -ed',
                           'Adjectives & Adverbs with exceptions well hard',
                           'So & such, enough & too the same, as', 'Comparison adjectives',
                           'Superlative adjectives', 'Comparison - much better/any better/ the sooner.. the better etc',
                           'Comparison - as..as, not so..as. like, than', 'Still/yet/already/any more etc',
                           'Viewpoint and commenting adverbs', 'Adverbs of Certainty'
                           ]
# here
list_verb = ['🔙back', 'Verb + V-ing', 'Verb + to V', 'Complex object: Verb (+ object) + to V',
             'Verb + V-ing or to V', 'Preposition (in/for/about etc.) + V-ing',
             'To..,for..and so that', 'Adjective + to V']

list_modal_verbs = ['🔙back', 'Can/could/be able to + V', ' Could(do)/could have (done)',
                    "Must/can't/have to/needn't", 'May and Might', 'Should/would/had better',
                    'Requests/offers/permission/invitations']

list_tenses = ['🔙back', 'Present simple', 'Present Continuous', 'Present perfect/continuous',
               'Past simple', 'Past continuous', 'Past perfect', 'Past Perfect continuous',
               'Future simple/to be going to', 'Future continuous/perfect continuous',
               'Construction: used to']

list_passive = ['🔙back', 'Passive Present', 'Passive Past', 'Passive Future']

list_reported_speech = ['🔙back', 'Reported Statements',
                        'Reported Questions', 'Reported Orders/Requests']

list_tag = ['🔙back', 'Tag Question', 'I think so/I have so etc']

list_clauses = ['🔙back', 'Relative clauses  who/that/which', 'Clauses with & without who/that/which',
                'Clauses whose/whom/where', 'Clauses: extra information',
                'Clauses V-ing/V-ed(gerund, participle)']

list_conjunction_preposition = ['🔙back', 'Although/though/even though/in split of/despite',
                                'Unless/As long as/provided/providing/in case',
                                'As/like and as/as if/as though', 'For/during and while',
                                'By/until', 'At/on/in/on in time/at the end & in the end(time)',
                                'In/at/on/by(position)', 'To/at/in/into(direction)', 'In/on/at(other uses)',
                                'Noun + preposition', 'Adjective + preposition', 'Verb + preposition',
                                ]
list_completions = ['🔙back', 'Sentence completion', 'Dialogue Completion',
                    'Text completion(missing part)', 'Text completion(right form of the verb)']

list_gap_filling = ['🔙back', 'Gap filling(right form of the verb)', 'Gap filling(mixed:nouns, verb, Preposition etc)',
                    'Gap filling(choose the right part of speech)']

lists = ['Numerals',
         'Subjunctive mood/ unreal wishes(i wish)',
         'Conditional sentences',
         'Give the right definition/synonym/antonym etc',
         ]

dict_nov_bar = {
    'Nouns💡': list_nouns,
    'Articles': list_articles,
    'Pronouns': list_pronouns,
    'Quantifiers': list_quantifiers,
    'Adjectives and adverbs': list_Adjectives_adverbs,
    'Verb': list_verb,
    'Modal verbs': list_modal_verbs,
    'Tenses': list_tenses,
    'Passive voice': list_passive,
    'Reported speech': list_reported_speech,
    'Tag questions': list_tag,
    'Clauses': list_clauses,
    'Conjunction and Preposition': list_conjunction_preposition,
    'Gap filling': list_gap_filling

}

main_topic = [
    'назад',
]
main_topic.extend(dict_nov_bar.keys())
