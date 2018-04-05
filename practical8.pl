road(birmingham,bristol, 9).
road(london,birmingham, 3).
road(london,bristol, 6).
road(london,plymouth, 5).
road(plymouth,london, 5).
road(portsmouth,london, 4).
road(portsmouth,plymouth, 8).
get_road(Start, End, Visited, Result) :-
    get_road(Start, End, [Start], 0, Visited, Result).
get_road(Start, End, Waypoints, DistanceAcc, Visited, TotalDistance) :-
    road(Start, End, Distance),
    reverse([End|Waypoints], Visited),
    TotalDistance is DistanceAcc + Distance.
get_road(Start, End, Waypoints, DistanceAcc, Visited, TotalDistance) :-
    road(Start, Waypoint, Distance),
    \+ member(Waypoint, Waypoints),
    NewDistanceAcc is DistanceAcc + Distance,
    get_road(Waypoint, End, [Waypoint|Waypoints], NewDistanceAcc, Visited, TotalDistance).
