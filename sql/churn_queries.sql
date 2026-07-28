-- ============================================================
-- SQL Business Analytics & Churn Insights
-- Database: churn.db | Table: customers
-- ============================================================

-- 1. Overall Churn Rate Summary
SELECT 
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    COUNT(*) - SUM(Churn) AS retained_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers;

-- 2. Churn Rate by Customer Status (1 = Active, 2 = Inactive)
SELECT 
    CASE Status 
        WHEN 1 THEN 'Active'
        WHEN 2 THEN 'Inactive'
        ELSE 'Unknown'
    END AS status_label,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers
GROUP BY Status;

-- 3. Churn Rate by Complaint Status (0 = No Complaint, 1 = Complained)
SELECT 
    CASE Complains 
        WHEN 0 THEN 'No Complaints'
        WHEN 1 THEN 'Has Complained'
    END AS complaint_status,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers
GROUP BY Complains;

-- 4. Average Usage Metrics by Churn Status
SELECT 
    CASE Churn 
        WHEN 1 THEN 'Churned'
        ELSE 'Retained'
    END AS churn_status,
    ROUND(AVG("Seconds of Use"), 2) AS avg_seconds_of_use,
    ROUND(AVG("Frequency of use"), 2) AS avg_frequency_of_use,
    ROUND(AVG("Distinct Called Numbers"), 2) AS avg_distinct_calls,
    ROUND(AVG("Customer Value"), 2) AS avg_customer_value,
    ROUND(AVG("Revenue_Per_Month"), 2) AS avg_monthly_revenue
FROM customers
GROUP BY Churn;

-- 5. High-Value Customers at Risk of Churn
SELECT 
    "Subscription Length",
    "Customer Value",
    "Revenue_Per_Month",
    "Complains",
    "Status",
    "Frequency of use"
FROM customers
WHERE Churn = 1 AND "Customer Value" > (SELECT AVG("Customer Value") FROM customers)
ORDER BY "Customer Value" DESC
LIMIT 10;

-- 6. Total Monthly Revenue Loss due to Churn
SELECT 
    ROUND(SUM("Revenue_Per_Month"), 2) AS total_monthly_revenue_lost,
    ROUND(SUM("Customer Value"), 2) AS total_customer_value_lost
FROM customers
WHERE Churn = 1;
