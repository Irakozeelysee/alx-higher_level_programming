#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = Py_SIZE(p);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AS_STRING(p));
	printf("  first 10 bytes:");

	if (size > 10)
		size = 10;

	for (i = 0; i < size; i++)
	{
		printf(" %.2x", bytes->ob_sval[i]);
	}

	printf("\n");
}
