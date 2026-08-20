def sql_policy_validator(state: AgentState) -> AgentState:
    """
    script to validate the statement
    """

    sql = state["proposed_sql"]

    if state["tool_calls"] > MAX_TOOL_CALLS:
        return # error case "Tool-call count is limited." past the error with state back to agentic then it will not write anymore sql. it will be enforce to leave as an system error at make decision if it call more tool and not provide asnwer yet.

    if have_mutiple_statement(sql) == True :
        return # error case "Only one SQL statement is allowed." past the error with state back to agentic

    if get_statement_type(sql) != "SELECT":
        return # error case "Only read-only SELECT is allowed." past the error with state back to agentic

    if contains_disallowed_table_or_column(sql):
        return # error case "Query accesses an unauthorized source." past the error with state back to agentic

    if contains_select_all(sql):
        return # error case "SELECT * is not allowed." past the error with state back to agentic

    if get_estimated_cost(sql) > MAX_QUERY_COST:
        return # error case "Query is too expensive." past the error with state back to agentic

    return {
        **state, 
    } # wire with small_llm_reviewer
