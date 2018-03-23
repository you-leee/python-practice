class BinaryHeap:
    def __init__(self):
        self.elems = []

    def hpush(self, elem):
        self.elems.append(elem)

        position = len(self.elems) - 1
        parent_idx = position
        while parent_idx > 0:
            parent_idx = self.__parent_idx(parent_idx)
            if self.elems[parent_idx] >= elem:
                return
            self.__swap(position, parent_idx)

            position = parent_idx

    def hpop(self):
        if len(self.elems) == 0:
            raise IndexError('Pop from empty heap')

        popped = self.elems[0]
        self.elems[0] = self.elems[len(self.elems) - 1]
        self.elems.pop()

        position = 0
        largest_child_idx = self.largest_child_idx(position)
        while largest_child_idx is not None:
            if self.elems[largest_child_idx] <= self.elems[position]:
                break

            self.__swap(largest_child_idx, position)
            position = largest_child_idx
            largest_child_idx = self.largest_child_idx(position)


        return popped

    def __swap(self, pos1, pos2):
        tmp = self.elems[pos1]
        self.elems[pos1] = self.elems[pos2]
        self.elems[pos2] = tmp


    def __parent_idx(self, idx):
        return (idx - 1)//2

    def __child_idxs(self, idx):
        max_idx = len(self.elems) - 1
        idxs = []
        base_idx = idx * 2
        if base_idx < max_idx:
            idxs.append(base_idx + 1)
        if (base_idx + 1) < max_idx:
            idxs.append(base_idx + 2)

        return idxs

    def largest_child_idx(self, idx):
        child_idxs = self.__child_idxs(idx)

        if len(child_idxs) == 0:
            return None

        if len(child_idxs) == 1:
            return child_idxs[0]

        if self.elems[child_idxs[0]] > self.elems[child_idxs[1]]:
            return child_idxs[0]
        else:
            return child_idxs[1]

    def __len__(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.hpush(1)
    bh.hpush(3)
    bh.hpush(5)
    bh.hpush(2)

    print(bh)

    bh.hpop()
    print(bh)