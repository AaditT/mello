# notes to emotion dictionary
# source: https://ledgernote.com/blog/lessons/musical-key-characteristics-emotions/
# Created by Aadit Trivedi

key_to_emotion = {
    'C Major': ['pure','happy','imaginative','earnest','simplicity'],
    'C Minor': ['love', 'languishing', 'longing','love-sick'],
    'C# Minor': ['despair', 'weeping', 'sorrow', 'grief'],
    'DB Major': ['depressive', 'sonority', 'euphony'],
    'D Major': ['triumphant', 'victorious', 'jubilation'],
    'D Minor': ['serious', 'pious', 'ruminating'],
    'D# Minor': ['distress', 'angst'],
    'EB Major': ['cruel', 'intimacy', 'devotion', 'honest'],
    'E Major': ['quarrelsome', 'boisterous'],
    'E Minor': ['effeminate', 'amorous', 'restless'],
    'F Major': ['furious', 'complaisance'],
    'F Minor': ['obscure', 'plaintive', 'funereal'],
    'F# Major': ['relief', 'success', 'clarity'],
    'F# Minor': ['gloomy', 'discontent', 'resentment'],
    'G Major': ['serious', 'magnificent', 'tender', 'satisfied'],
    'G Minor': ['uneasiness', 'worry', 'concern'],
    'AB Major': ['eternity', 'judgemental'],
    'AB Minor': ['lamentation', 'competition', 'moaning'],
    'A Major': ['joyful', 'pastoral', 'cheerful'],
    'A Minor': ['tender', 'soothing', 'graceful'],
    'BB Major': ['quaint', 'optimistic', 'hopeful'],
    'BB Minor': ['mocking', 'pessimism', 'surly'],
    'B Major': ['harsh', 'rage', 'strong', 'fury'],
    'B Minor': ['solitary', 'melancholic', 'patience'],   
}

def search(emotion):
    for key, value in key_to_emotion.items():
        if emotion in value:
            print key

search('melancholic')
