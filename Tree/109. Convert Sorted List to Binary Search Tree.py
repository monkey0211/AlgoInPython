class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_size(head):
    size = 0
    while head:
        size += 1
        head = head.next
    return size

def sorted_list_to_bst(head):
    # Function to convert linked list to BST
    def convert_list_to_bst(left, right):
        nonlocal head
        if left > right:
            return None
        
        mid = (left + right) // 2
        
        left_child = convert_list_to_bst(left, mid - 1)
        
        root = TreeNode(head.val)
        root.left = left_child
        
        head = head.next
        
        root.right = convert_list_to_bst(mid + 1, right)
        return root
    
    size = find_size(head)
    return convert_list_to_bst(0, size - 1)

# Helper function to print the tree in-order (for verification)
def in_order_traversal(root):
    result = []
    if root:
        result = in_order_traversal(root.left)
        result.append(root.val)
        result = result + in_order_traversal(root.right)
    return result

# Example usage
# Create a sorted linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

# Convert the linked list to a balanced BST
bst_root = sorted_list_to_bst(head)

# Print the in-order traversal of the BST (should print the numbers in sorted order)
print(in_order_traversal(bst_root))
