# -*- coding: utf-8 -*-
import time


class timerData:
    user_supply_data = {}

    def add_timer(self, author_id, business_type, resupply_time):
        try:
            author_data = user_supply_data[author_id]
        except KeyError:
            author_data = {}
        author_data[business_type] = resupply_time
        self.user_supply_data[author_id] = author_data

    # maybe add a confirmation if there is already a timer with the same type
    def get_elapsed_timer(self):  # return type and author_id of all elapsed timers
        out = []
        current_time = time.time()
        for author_id, author_data in self.user_supply_data.items():
            for business_type, resupply_time in author_data.items():
                if current_time >= resupply_time:
                    out.append({'type': business_type,
                                'author_id': author_id})
        for o in out:  # reset elapsed timer that are returned. must be in a new loop, because looped arrays can not be modified
            self.user_supply_data[o['author_id']][o['type']] = 0
        return out
