servesAll(american_restaurants, [salad, steak, sandwiches, burgers, fried_chicken]).
servesAll(burger_place_restaurants, [burgers, fries, onion_rings]).
servesAll(chinese_restaurants, [eggrolls, rice, shrimp, soup, noodles]).
servesAll(indian_restaurants, [papadam, bagan_bharta, rice, tandoori, naan]).
servesAll(italian_restaurants, [salad, pasta, cioppino, snapper, bread, garlic_bread]).
servesAll(japanese_restaurants, [sashimi, rice, tempura, noodles]).
servesAll(mediterranean_restaurants, [gyros, hummus, pita, falafel]).
servesAll(mexican_restaurants, [tacos, beans, rice, enchiladas, fish_tacos]).
servesAll(pizza_place_restaurants, [pizza, salad, garlic_bread]).
servesAll(thai_restaurants, [rice, noodles, larb, pad_thai]).

dishesAll(vegetarian_dishes, [beans, bagan_bharta, enchiladas, falafel, hummus, pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).
dishesAll(meat_dishes, [burgers, enchiladas, gyros, pad_thai, pizza, steak, sandwiches, fried_chicken, tacos, tandoori, larb]).
dishesAll(seafood_dishes, [snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]).
dishesAll(starch_dishes, [naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).

locationAll(fox_point, [pizza_marvin, bees, al_forno, dolores, tallulahs]).
locationAll(wayland, [red_stripe, pasta_beach, haruki, waterman_grille, lims]).
locationAll(thayer_street, [yans, bajas, andreas, chinatown, kabob_n_curry, heng, mikes, east_side_pocokets, shake_shack]).

cusineAll(chinese_restaurants, [yans, chinatown]).
cusineAll(burger_place_restaurants, [shake_shack]).
cusineAll(mexican_restaurants, [bajas, dolores, tallulahs]).
cusineAll(mediterranean_restaurants, [andreas, east_side_pocokets]).
cusineAll(indian_restaurants, [kabob_n_curry]).
cusineAll(thai_restaurants, [heng, lims]).
cusineAll(pizza_place_restaurants, [mikes, pizza_marvin]).
cusineAll(italian_restaurants, [pasta_beach, al_forno]).
cusineAll(japanese_restaurants, [haruki]).
cusineAll(american_restaurants, [red_stripe, waterman_grille]).

serves(Kind, Dish) :-
    servesAll(Kind, Dishes),
    member(Dish, Dishes).

dishes(Kind, Dish) :-
    dishesAll(Kind, Dishes),
    member(Dish, Dishes).

locations(Location, Restaurant) :-
    locationAll(Location, Restaurants),
    member(Restaurant, Restaurants).

cuisines(Kind, Restaurant) :-
    cusineAll(Kind, Restaurants),
    member(Restaurant, Restaurants).

type_of_dish_from_location(Location, Type_of_dish, Resturant_name) :-
    locations(Location, Resturant_name), 
    cuisines(Type_of_resturant, Resturant_name), 
    serves(Type_of_resturant, Dish), 
    dishes(Type_of_dish, Dish).

/**
1. Which restaurants are in wayland?
locations(wayland, X).
2. Which restaurants have italian cuisine?
cuisines(italian_restaurants, X).
3. Which kind of restaurants serve snapper?
serves(X, snapper).
4. Which kinds of restaurants serves rice ?
serves(X, rice).
5. Where can you get served a vegetarian dish in fox_point?
type_of_dish_from_location(fox_point, vegetarian_dishes).

Harder (Optional)
6. Which restaurants serve both vegetarian and meat dishes?

7. Which areas have both a chinese restaurant and a mexican restaurant?

8. Which restaurants on thayer_street or in wayland serve meat dishes?

9. Which restaurants in wayland don't serve bread?

10. Which areas have more than one restaurant of some type of cuisine?

11. Which areas have more than one restaurant serving noodles?

*//