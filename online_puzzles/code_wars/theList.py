# from time import sleep
# class Dinglemouse(object):

#     def __init__(self, queues, capacity):
#         # 1 for up, -1 for down
#         self.queues = [ list(q) for q in queues]
#         self.pessenger_count = sum([len(q) for q in queues])
#         self.container = []
#         self.capacity = capacity
#         print(self.queues, self.pessenger_count, self.capacity)
        

#     def _discharge_container(self, pos):
#         discharged = False
#         for i in range(len(self.container)-1 , -1, -1):
#             if self.container[i] == pos:
#                 self.pessenger_count -= 1
#                 self.container.pop(i)
#                 discharged = True
#         return discharged

#     def _charge_container(self, pos, direction):
#         condition = direction > 0
#         slot_left = self.capacity - len(self.container)
#         if slot_left == 0:
#             return
#         pop_list = []
#         for i, c in enumerate(self.queues[pos]):
#             if (c > pos) == condition:
#                 print("charge", c, pos, direction)
#                 pop_list.append(i)
#                 self.container.append(c)
#                 slot_left -= 1
#         charged = True if len(pop_list) else False
#         # clean_queues
#         for i in reversed(pop_list):
#             self.queues[pos].pop(i)
#         return charged
        
#     def theLift(self):
#         result = [0]
#         pos = 0
#         direction = 1
#         while True:
#             pos += direction
#             discharged = self._discharge_container(pos)
#             charged = self._charge_container(pos,direction)
#             if discharged or charged:
#                 result.append(pos)
#             if self.pessenger_count == 0:
#                 break
#             if pos == len(self.queues)-1 or pos == 0:
#                 direction = -direction            
#         if result[-1] != 0:
#             result.append(0)
#         return result


tests = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
  
# for queues, answer in tests:
#     lift = Dinglemouse(queues, 5)
#     print(lift.theLift() == answer)
    
# the lift version 2

class Dinglemouse(object):
    def __init__(self, queues, capacity):
        # 1 for up, -1 for down
        print(queues, capacity)
        self.qs = [(i,list(q)) for i, q in enumerate(queues) if q]
        self.q_pos = 0
        self.lift = []
        self.cap = capacity
        self.dir = 1        
        self.result = [0]     

    def _condition(self):
        return self.dir > 0
    
    def _add_result(self, floor: int):
        if self.result[-1] != floor:
            self.result.append(floor)
            
    def _ordered_lift_append(self, c):
        for i, l in enumerate(self.lift):
            if c <= l:
                self.lift.insert(i, c)
                return
        self.lift.append(c)
        
    def _charge(self):
        f, q = self.qs[self.q_pos]
        pop_list = []

        for i, c in enumerate(q):
            if (c > f) == self._condition():
                if len(self.lift) < self.cap:
                    pop_list.append(i)
                    self._ordered_lift_append(c)
                self._add_result(f)
        for i in reversed(pop_list):
            q.pop(i)
        if not q:
            self.qs.pop(self.q_pos)
            if self.dir == 1:
                self.q_pos -= 1

    def _discharge(self):
        if not self.qs:
            self._discharge_all()
            return
        floor = self.qs[self.q_pos][0]
        if self._condition():
            while self.lift and self.lift[0] <= floor:
                self._add_result(self.lift.pop(0))
        else:
            while self.lift and self.lift[-1] >= floor:
                self._add_result(self.lift.pop(-1))

    def _discharge_all(self):
        pop_pos = 0 if self._condition() else -1
        while self.lift:
            self._add_result(self.lift.pop(pop_pos))

    def _move(self):
        self.q_pos += self.dir
        if not self.qs:
            return
        if self.q_pos == len(self.qs) or self.q_pos == -1:
            self._discharge_all()
            self.dir = -self.dir
            self.q_pos += self.dir
            
    def theLift(self):
        while self.qs:
            self._charge()
            self._move()
            self._discharge()
        self._add_result(0)
        return self.result
            
            
more_test = [
    [
        ((4, 15, 11), (), (10, 9, 6, 1), (1,), (12, 3, 11, 13), (1, 9, 13, 4, 14), (9, 5, 2, 7, 8), (2, 4, 4), (14, 4, 16, 0, 9), (5,), (7, 15), (3,), (0, 10), (15, 3, 3, 12, 1), (12, 0, 13, 7), (14,), (12, 9, 8)),
        4, 
        [0, 2, 4, 5, 6, 8, 10, 11, 12, 13, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 2, 4, 5, 6, 8, 9, 11, 13, 14, 13, 11, 8, 7, 6, 5, 4, 3, 0, 5, 6, 7, 8, 9, 13, 14, 13, 12, 11, 8, 7, 6, 5, 4, 3, 1, 0, 6, 8, 9, 16, 6, 5, 4, 2, 0]
             ],
    ]   
            
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    print(lift.theLift(), answer, end=" ")
    print(lift.theLift() == answer)