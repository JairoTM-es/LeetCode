With SalariosRankeados As (
    Select Department.Name AS Department,
        Employee.Name AS Employee,
        Employee.Salary,
        DENSE_RANK() Over (Partition by Department.Id order by Employee.Salary DESC) AS RankSalarios
        From Employee Join Department ON Employee.departmentId = Department.Id
)Select Department,Employee,Salary From SalariosRankeados Where RankSalarios <= 3
