import random
from consts import *


class Player(GamePlayer):

    def __init__(self):
        self.name = "Player"
        self.group = "n/a"

    def step(self, game_map, turn, cur_pos):

        position_objects = {'banana': [], 'coin': [], 'cauldron': []}
        position_players = {}
        banana_count = 0
        coin_count = 0
        cauldron_count = 0
        players_count = 0

        for row in game_map:

            for element in row:

                if len(element) > 0 and type(element[0]) == GameObject:

                    if element[0].obj_type == 0:
                        key_title = "banana"

                        position_objects[key_title].append(element[0].position)
                        banana_count += 1

                    elif element[0].obj_type == 1:
                        key_title = "coin"
                        position_objects[key_title].append(element[0].position)
                        coin_count += 1

                    elif element[0].obj_type == 2:
                        key_title = "cauldron"
                        position_objects[key_title].append(element[0].position)
                        cauldron_count += 1

                elif len(element) > 0 and type(element[0]) == Bot:

                    position_players[element[0]] = element[0].position
                    players_count += 1

        # Defines new variables at turn 0.
        if turn == 0:
            self.ban_count = banana_count
            self.co_count = coin_count
            self.cau_count = cauldron_count

        # Sets a direction to move depending on the location of the target object.
        def get_direction_tuple(x, y):
            if x > cur_pos[0]:
                direction_row = "down"

            if x < cur_pos[0]:
                direction_row = "up"

            if x == cur_pos[0]:
                direction_row = 0

            if y > cur_pos[1]:
                direction_col = "right"

            if y < cur_pos[1]:
                direction_col = "left"

            if y == cur_pos[1]:
                direction_col = 0

            return (direction_row, direction_col)

        # Calculates the distance between two coordinates.
        def calc_distance(coords1, coords2):
            return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

        # A helper function that finds the closest object of every type to the player.
        def closest_objects():
            position_closest_objects = {'banana': [], 'coin': [], 'cauldron': []}

            for key in position_closest_objects:
                distances = []

                if len(position_objects[key]) > 0:

                    for i in range(len(position_objects[key])):

                        distance = calc_distance(position_objects[key][i], cur_pos)
                        distances.append(distance)

                    min_distance = min(distances)

                    for i in range(len(position_objects[key])):

                        if calc_distance(position_objects[key][i], cur_pos) == min_distance:
                            position_closest_objects[key].append(position_objects[key][i])

            return position_closest_objects

        def collection_stop(object_type):
            list_objects_present_in_map = ['banana', 'coin', 'cauldron']

            index_object_type = list_objects_present_in_map.index(object_type)

            if object_type == 'banana':
                amount_objects = self.ban_count
                var_count = banana_count

            elif object_type == 'coin':
                amount_objects = self.co_count
                var_count = coin_count

            elif object_type == 'cauldron':
                amount_objects = self.cau_count
                var_count = cauldron_count

            for bot in position_players:
                if bot.collected_objects[index_object_type] > (amount_objects / players_count):
                    return True

            if var_count == 0:
                return True

            return False

        def find_target_obj():
            closest_dict = closest_objects()

            # Checks if we still want to collect bananas.
            if not collection_stop('banana'):

                # Checks if the amount of bananas is the smallest count.
                if banana_count <= min(coin_count, cauldron_count):

                    # Sets the target type to "banana"
                    target_type = "banana"

                    # Sets the new closest target to "banana"
                    closest_target = closest_dict[target_type]

                # If we want to stop collecting coins and cauldrons,
                # we set the target type to "banana"
                elif collection_stop('coin') and collection_stop('cauldron'):
                    target_type = "banana"
                    closest_target = closest_dict[target_type]

                # If we want to stop collecting cauldrons and if we have less
                # bananas in the map than coins.
                elif collection_stop('cauldron') and banana_count <= coin_count:
                    target_type = "banana"
                    closest_target = closest_dict[target_type]

                # If we want to stop collecting coins and if we
                # have less bananas in the map than cauldrons.
                elif collection_stop('coin') and banana_count <= cauldron_count:
                    target_type = "banana"
                    closest_target = closest_dict[target_type]

                # If we want to stop collecting cauldrons and if
                # the amount of bananas in the map is less than the amount of cauldrons.
                elif collection_stop('cauldron') and banana_count <= cauldron_count:
                    target_type = "banana"
                    closest_target = closest_dict[target_type]

                # If we want to stop collecting coins and
                # if there are less bananas than coins.
                elif collection_stop('coin') and banana_count <= coin_count:
                    target_type = "banana"
                    closest_target = closest_dict[target_type]

            # Checks if we are still collecting coins.
            if not collection_stop('coin'):

                # Checks if the amount of coins is the smallest count.
                if coin_count <= min(banana_count, cauldron_count):
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting bananas and cauldrons.
                elif collection_stop('banana') and collection_stop('cauldron'):
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting cauldrons and
                # if we have less coins than cauldrons.
                elif collection_stop('cauldron') and coin_count <= cauldron_count:
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting bananas and
                # if we have less coins than bananas.
                elif collection_stop('banana') and coin_count <= banana_count:
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting cauldrons and
                # if we have less coins than bananas.
                elif collection_stop('cauldron') and coin_count <= banana_count:
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting bananas and
                # if we have less coins than cauldrons.
                elif collection_stop('banana') and coin_count <= cauldron_count:
                    target_type = "coin"
                    closest_target = closest_dict[target_type]

            # Checks if we should continue collecting cauldrons.
            if not collection_stop('cauldron'):

                # Checks if the amount of cauldrons is the small amount.
                if cauldron_count <= min(banana_count, coin_count):
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

                # Checks if we should stop collecting bananas and coins.
                elif collection_stop('banana') and collection_stop('coin'):
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting bananas and
                # if we have less cauldrons than coins.
                elif collection_stop('banana') and cauldron_count <= coin_count:
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting coins and
                # if we have less cauldrons than coins.
                elif collection_stop('coin') and cauldron_count <= coin_count:
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting bananas and
                # if we have less cauldrons than bananas.
                elif collection_stop('banana') and cauldron_count <= banana_count:
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

                # Checks if we want to stop collecting coins and
                # if we have less cauldrons than coins.
                elif collection_stop('coin') and cauldron_count <= banana_count:
                    target_type = "cauldron"
                    closest_target = closest_dict[target_type]

            # Checks if we should stop collecting cauldrons, bananas and coins.
            if collection_stop('cauldron') and collection_stop('banana') and collection_stop('coin'):
                list_of_remaining_types = []

                # Goes through every object inside "closest_dict".
                for key in closest_dict:

                    # Checks if we have at least one position for the given key.
                    if len(closest_dict[key]) >= 1:
                        list_of_remaining_types.append(key)

                # We choose a random target between the given objects.
                target_type = random.choice(list_of_remaining_types)

                # Defines the closest target.
                closest_target = closest_dict[target_type]

            return (target_type, closest_target[0][0], closest_target[0][1])

        # Calculates the direction the bot should take.
        def next_direction(direction_tuple):

            # Choosing a random direction for the next move if the target
            # object is not in the same row nor in the same column.
            if type(direction_tuple[0]) == str and type(direction_tuple[1]) == str:
                return random.choice([direction_tuple[0], direction_tuple[1]])

            # Checks if the first element of the tuple is a string.
            elif type(direction_tuple[0]) == str:
                return direction_tuple[0]

            else:
                return direction_tuple[1]

        # Chooses the optimal path
        def optimal_path():
            target_obj = find_target_obj()
            target_tuple = (target_obj[1], target_obj[2])
            closest_objs = closest_objects()

            opt_closest_objs = []

            # Checks if we should stop collecting cauldrons, bananas and coins, which means that we won.
            if collection_stop('cauldron') and collection_stop('banana') and collection_stop('coin'):
                # Gets the direction our player should be heading towards.
                direction_tuple = get_direction_tuple(int(target_obj[1]), int(target_obj[2]))
                return next_direction(direction_tuple)

            # Goes through the objects inside "closest_objs"
            for obj in closest_objs:

                # If an object tuple has no remaining objects, we skip it.
                if len(closest_objs[obj]) != 0:

                    # Goes through the positions of every closest item.
                    for multiple_objs in closest_objs[obj]:
                        obj_tuple = multiple_objs

                        # Checks if the distance between the player and the target object
                        # is bigger than the distance between the closest object and the target object.
                        if calc_distance(target_tuple, obj_tuple) < calc_distance(target_tuple,(cur_pos[0], cur_pos[1])):
                            opt_closest_objs.append(obj_tuple)

                    # Checks if we only have one object in the list "opt_closest_objs".
                    if len(opt_closest_objs) == 1:
                        opt_closest_obj = opt_closest_objs[0]

                        # We move to this object.
                        direction_tuple = get_direction_tuple(opt_closest_obj[0], opt_closest_obj[1])
                        return next_direction(direction_tuple)

                    # We have more than one object in the list "opt_closest_objs".
                    elif len(opt_closest_objs) > 1:

                        # Move to a random selected object
                        opt_closest_obj = random.choices(opt_closest_objs)[0]
                        direction_tuple = get_direction_tuple(opt_closest_obj[0], opt_closest_obj[1])
                        return next_direction(direction_tuple)

            if len(opt_closest_objs) == 0:

                # Move closer to target without getting any objects
                direction_tuple = get_direction_tuple(int(target_obj[1]), int(target_obj[2]))
                return next_direction(direction_tuple)

        return optimal_path()