#include "lists.h"
#include <stddef.h>
/**
 * insert_node - insert a node in a sorted list
 * @head: pointer to head
 * @number: number to insert
 * Return: address of the new node or NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = malloc(sizeof(listint_t));
	listint_t *past;

	current->n = number;
	if (!head)
	{
		*head = current;
		current->next = NULL;
		return (current);
	}
	current->next = (*head)->next;
	past = *head;
	if (!current->next)
	{
		(*head)->next = current;
		return (current);
	}
	while (current->next)
	{
		if ((current->next)->n > number)
		{
			past->next = current;
			return (current);
		}
		past = past->next;
		current->next = (current->next)->next;
	}
	past->next = current;
	return (current);
}
