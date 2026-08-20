def make_decision(state: AgentState) -> AgentState:
    """
    this is "contain tool calling or not node" in pic 1
    the final_response will be use as a exit condition 
    """
    iter_call = state.get("tool_calls", 0)

    if state.requests_sql_tool:
        if iter_call >= MAX_TOOL_CALLS:
            raise # exceed a number of tool calling case 
        return {
            **state,
            "tool_calls": iter_call + 1,
            "state_memory": state.get("state_memory").append({"sql" : sql, "preview_sql" : preview_sql})
            } #connect with  sql_policy_validator

    return {
            **state,
            "final_response": state.structured_response
        } # connect with frontend_render_formater
