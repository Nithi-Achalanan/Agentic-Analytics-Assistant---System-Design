def postgres_sql(state: AgentState) -> AgentState:
    """
    Execute validated SQL against PostgreSQL.
    """

    try:
        result = db.execute(
            sql=state["proposed_sql"],
            role="analytics_read_only",
            timeout_seconds=5,
            max_rows=MAX_RESULT_ROWS
        )

        return {
            **state,
            "sql_result": result,
            "sql_preview": result.first(10), # agentic summary only head
        }

    except DatabaseTimeout:
        return # time out error case agent must retire it.

    except DatabaseError:
        return   # DatabaseError case agent must retire it with the description of the error so it can be avoided.
