# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        return [sequence]
    else:
        return [character + permutation for character in sequence for permutation in get_permutations(sequence.replace(character, ''))]
            
if __name__ == '__main__':
   # Put three example test cases here (for your sanity, limit your inputs
   # to be three characters or fewer as you will have n! permutations for a 
   # sequence of length n)

   example_input = 'labs'
   print('Input:', example_input)
   expected_output = ['labs', 'lasb', 'lbas', 'lbsa', 'lsab', 'lsba', 'albs', 'alsb', 'abls', 'absl', 'aslb', 'asbl', 'blas', 'blsa', 'bals', 'basl', 'bsla', 'bsal', 'slab', 'slba', 'salb', 'sabl', 'sbla', 'sbal']
   print('Expected Output:', expected_output)
   output = get_permutations(example_input)
   print('Output:', output)
   print('Equal:', set(output) == set(expected_output))

   print('=' * 40)

   example_input = 'poiu'
   print('Input:', example_input)
   expected_output = ['poiu', 'poui', 'piou', 'piuo', 'puoi', 'puio', 'opiu', 'opui', 'oipu', 'oiup', 'oupi', 'ouip', 'ipou', 'ipuo', 'iopu', 'ioup', 'iupo', 'iuop', 'upoi', 'upio', 'uopi', 'uoip', 'uipo', 'uiop']
   print('Expected Output:', expected_output)
   output = get_permutations(example_input)
   print('Output:', output)
   print('Equal:', set(output) == set(expected_output))

   print('=' * 40)

   example_input = 'pkc'
   print('Input:', example_input)
   expected_output = ['pkc', 'pck', 'kpc', 'kcp', 'cpk', 'ckp']
   print('Expected Output:', expected_output)
   output = get_permutations(example_input)
   print('Output:', output)
   print('Equal:', set(output) == set(expected_output))


