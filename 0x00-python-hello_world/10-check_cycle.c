#include "lists.h"
/**
* check_cycle - checks for a cycle in a list
* @list: list
* Return: 0 if there is no cycle
*         1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
listint_t *wow = list;
listint_t *hello = list;

while (hello && wow && wow->next)
{
wow = wow->next->next;
hello = hello->next;
if (wow == hello)
return (1);
}
return (0);
}
