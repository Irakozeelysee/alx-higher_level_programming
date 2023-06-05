#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check-cycle - checks if there is a cycle in our list.
 * @list: pointer
 * Return: 0 for no cycle and 1 for there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
