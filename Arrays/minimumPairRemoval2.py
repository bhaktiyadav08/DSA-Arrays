import heapq

class Node:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
        self.prev = None
        self.next = None
        self.deleted = False

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        
        # Build doubly linked list
        nodes = [Node(nums[i], i) for i in range(n)]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]
        
        # Count initial decreases
        decrease_count = sum(1 for i in range(n - 1) if nums[i] > nums[i + 1])
        
        if decrease_count == 0:
            return 0
        
        # Priority queue: (cost, idx1, idx2, value1, value2)
        # Store original values to detect stale entries
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nums[i] + nums[i + 1], i, i + 1, nums[i], nums[i + 1]))
        
        merges = 0
        
        while decrease_count > 0 and pq:
            cost, idx1, idx2, val1, val2 = heapq.heappop(pq)
            
            node1, node2 = nodes[idx1], nodes[idx2]
            
            # Skip stale entries
            if (node1.deleted or node2.deleted or 
                node1.value != val1 or node2.value != val2 or
                node1.next != node2):
                continue
            
            # Perform merge
            merges += 1
            merged_value = cost
            
            # Update decrease count
            if node1.value > node2.value:
                decrease_count -= 1
            
            prev_node = node1.prev
            next_node = node2.next
            
            # Check decrease changes with prev
            if prev_node and not prev_node.deleted:
                old_decreases = (prev_node.value > node1.value)
                new_decreases = (prev_node.value > merged_value)
                if old_decreases and not new_decreases:
                    decrease_count -= 1
                elif not old_decreases and new_decreases:
                    decrease_count += 1
            
            # Check decrease changes with next
            if next_node and not next_node.deleted:
                old_decreases = (node2.value > next_node.value)
                new_decreases = (merged_value > next_node.value)
                if old_decreases and not new_decreases:
                    decrease_count -= 1
                elif not old_decreases and new_decreases:
                    decrease_count += 1
            
            # Update linked list
            node1.value = merged_value
            node2.deleted = True
            node1.next = next_node
            if next_node:
                next_node.prev = node1
            
            # Add new pairs to priority queue
            if prev_node and not prev_node.deleted:
                heapq.heappush(pq, (prev_node.value + merged_value, 
                                   prev_node.idx, node1.idx, 
                                   prev_node.value, merged_value))
            
            if next_node and not next_node.deleted:
                heapq.heappush(pq, (merged_value + next_node.value, 
                                   node1.idx, next_node.idx, 
                                   merged_value, next_node.value))
        
        return merges