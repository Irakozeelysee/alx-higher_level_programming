#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;
	
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;
	
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02x", string[i] & 0xff);
	printf("\n");
}
