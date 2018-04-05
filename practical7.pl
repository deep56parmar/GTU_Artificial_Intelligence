
tiles(Row1,Row2,Row3).
move(tiles(R1,R2,R3),
     tiles(R4,R5,R6)).
bfs(State, Goal, Path) :-
    bfs_help([[State]], Goal, RevPath),
    reverse(RevPath, Path).

bfs_help([[Goal|Path]|_], Goal, [Goal|Path]).
bfs_help([Path|RestPaths], Goal, SolnPath) :-
    extend(Path, NewPaths),
    append(RestPaths, NewPaths, TotalPaths),
    bfs_help(TotalPaths, Goal, SolnPath).

extend([State|Path], NewPaths) :-
    bagof([NextState,State|Path], move(State,NextState), NewPaths), !.
extend(_, []).

