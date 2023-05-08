#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if there is a cycle in a singly  linked list
 * @list: pointer to the list
 * Return: 0 if there is no cycle 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	int i = 0, j;
	listint_t **past;

	if (!list)
		return (0);
	past = malloc(sizeof(listint_t *));
	past[0] = list;
	i++;
	while (list->next != NULL)
	{
		list = list->next;

		for (j = 0; j < i; j++)
		{
			if (past[j] == list)
			{
				free(past);
				return (1);
			}
		}
		past = realloc(past, sizeof(listint_t *) * (1 + i));
		past[i] = list;
		i++;
	}
	free(past);
	return (0);
}
