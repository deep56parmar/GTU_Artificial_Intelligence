solution(_, []).
solution(N, [X/Y|Others]) :-
    solution(N, Others),
    between(1, N, Y),
    noattack(X/Y, Others).

noattack(_,[]).
noattack(X/Y, [X1/Y1 | Others]) :-
    Y =\= Y1,
    Y1-Y =\= X1-X,
    Y1-Y =\= X-X1,
    noattack( X/Y, Others).

template(N, L) :-
    findall(I/_, between(1,N,I), L).
