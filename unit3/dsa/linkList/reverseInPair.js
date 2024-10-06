// reverse in pair 
const LinkedListNode = class {
  constructor(nodeData) {
    this.data = nodeData;
    this.next = null;
  }
};
// Complete the function below
var reversePair = function (head) {
  if (head == null || head.next == null) {
    return head;
  }
  let dummy = new LinkedListNode(0);
  dummy.next = head;

  prev = dummy;
  curr = head;

  while (curr != null && curr.next != null) {
    let nextNode = curr.next;
    curr.next = nextNode.next;

    nextNode.next = curr;
    prev.next = nextNode;

    prev = curr;
    curr = curr.next;
  }
  head = dummy.next;
  return head;
};
