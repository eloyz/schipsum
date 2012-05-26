

def detail(request, **kwargs):
    from random import choice
    from itertools import chain
    from django.template import RequestContext
    from django.shortcuts import render_to_response
    from ipsum.models import Phrase

    phrases = Phrase.objects.filter(approved=True).order_by('?')
    phrases = list(chain(phrases, phrases, phrases))

    sentence = u''
    sentences = []

    conjuctions = [
        'and',
        'though',
        'however',
        'but',
        'eventually',
        'especially',
        'afterwards',
        'so that',
        'but while',
    ]

    for phrase in phrases:

        pk = phrase.pk
        phrase = phrase.phrase

        phrase = phrase.strip('\n')

        if pk % 3:
            phrase = '%s, %s' % (phrase, choice(conjuctions))

        if not sentence:
            phrase = '%s%s' % (phrase[0].capitalize(), phrase[1:])

        sentence = '%s %s' % (sentence, phrase)

        if not pk % 3:
            sentence = sentence + u'.'
            sentences.append(sentence)
            sentence = u''

    paragraph = u''
    paragraphs = []
    for i, sentence in enumerate(sentences):

        paragraph = '%s %s' % (paragraph, sentence)

        if not i % 4 and i > 0:
            paragraphs.append(paragraph)
            paragraph = u''

    return render_to_response(
        'detail.html',
        {'paragraphs': paragraphs},
        context_instance=RequestContext(request)
    )
