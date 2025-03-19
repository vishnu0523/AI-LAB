% Forward Chaining in Prolog

% Facts
fact(sunny).
fact(warm).
fact(high_humidity).

% Rules
rule(happy) :- fact(sunny), fact(warm).
rule(go_swimming) :- fact(happy), fact(high_humidity).

% Forward Chaining Inference Engine
forward_chain :-
    assert_new_facts,
    write('Derived Facts: '),
    findall(F, fact(F), Facts),
    writeln(Facts).

assert_new_facts :-
    rule(Fact),
    \+ fact(Fact),
    assertz(fact(Fact)),
    assert_new_facts.
assert_new_facts.

% Sample query to run the program
% ?- forward_chain.
